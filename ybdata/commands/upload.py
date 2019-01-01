# ybdata.commands.upload
# Upload datasets to S3 bucket
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 14:35:04 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: upload.py [] benjamin@bengfort.com $

"""
Upload datasets to S3 bucket
"""

##########################################################################
## Imports
##########################################################################

import os
import re
import json
import boto3

from commis import Command
from commis.exceptions import ConsoleError

from ybdata.utils import urljoin


VERS = re.compile(r'^v(\d+)\.(\d+)(\.\d+)?$')
S3PRE = "https://s3.amazonaws.com/"
BUCKET = "ddl-data-lake"


##########################################################################
## Command
##########################################################################


class UploadCommand(Command):

    name = "upload"
    help = "upload datasets to S3 and update manifold"
    args = {
        ("-b", "--bucket"): {
            "default": BUCKET, "help": "s3 bucket to upload data to",
        },
        ("-u", "--uploads"): {
            "default": "./uploads", "metavar": "PATH",
            "help": "uploads directory to packge data to",
        },
        ("-a", "--all"): {
            "action": "store_true", "default": False,
            "help": "(re)upload all datasets in the uploads directory",
        },
        ("-p", "--pending"): {
            "action": "store_true", "default": False,
            "help": "upload pending datasets with no URL in manifold",
        },
        ("-s", "--single"): {
            "type": str, "metavar": "PATH",
            "help": "upload a single dataset archive",
        },
        "version": {
            "help": "Yellowbrick version to associate datasets with"
        }
    }

    def handle(self, args):
        """
        Verify datasets and update manifold.json
        """
        version = args.version.lower()
        if not version.startswith("v"):
            version = "v"+version

        # Validate Version
        if VERS.match(version) is None:
            raise ConsoleError("'{}' does not match semantic versioning format".format(version))

        # Validate Arguments
        if sum([args.pending, args.all, bool(args.single)]) != 1:
            raise ConsoleError("specify one of --pending --all or --single")

        # Load manifold
        try:
            with open(os.path.join(args.uploads, "manifest.json")) as f:
                manifest = json.load(f)
        except Exception as e:
            raise ConsoleError("could not load manifold: {}".format(e))

        # Determine datasets to upload
        s3path = urljoin("yellowbrick", version)
        s3url = urljoin(S3PRE, args.bucket, s3path)
        datasets = []

        if args.all or args.pending:
            for name, meta in manifest.items():
                if args.pending and meta["url"].startswith(s3url):
                    continue
                datasets.append(name)
        else:
            if args.single in manifest:
                datasets.append(args.single)
            else:
                raise ConsoleError("no dataset named '{}' in manifest.json".format(args.single))

        # Upload the datasets to S3 and update the manifold
        s3 = boto3.client('s3')
        for dataset in datasets:
            # Figure out where the upload goes to
            meta = manifest[dataset]
            file = os.path.basename(meta["url"])
            src = os.path.join(args.uploads, file)
            dst = urljoin(s3path, file)

            # Upload using boto3
            s3.upload_file(src, args.bucket, dst, ExtraArgs={'ACL':'public-read'})

            # Update the manifold
            manifest[dataset]["url"] = urljoin(s3url, file)

        # Write the manifest back to disk
        with open(os.path.join(args.uploads, "manifest.json"), "w") as f:
            json.dump(manifest, f, indent=2)