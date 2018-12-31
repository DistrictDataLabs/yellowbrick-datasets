# ybdata.commands.package
# Package a dataset in preparation for upload.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 11:21:53 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: package.py [] benjamin@bengfort.com $

"""
Package a dataset in preparation for upload.
"""

##########################################################################
## Imports
##########################################################################

import os
import json
import shutil

from commis import color, Command
from commis.exceptions import ConsoleError

from ybdata.validate import is_valid
from ybdata.utils import sha256sum


##########################################################################
## Command
##########################################################################

class PackageCommand(Command):

    name = "package"
    help = "packages a dataset in preparation for upload"
    args = {
        ("-f", "--force"): {
            "action": "store_true", "default": False,
            "help": "ignore errors and force/overwite data packages",
        },
        ("-u", "--uploads"): {
            "default": "./uploads", "metavar": "PATH",
            "help": "uploads directory to packge data to",
        },
        "datasets": {
            "nargs": "+", "metavar": "DATA",
            "help": "paths to dataset directories for packaging",
        },
    }

    def handle(self, args):
        """
        Create packages for the specified datasets
        """

        # Ensure there is an uploads directory
        if not os.path.exists(args.uploads) or not os.path.isdir(args.uploads):
            if args.force:
                os.makedirs(args.uploads)
            else:
                raise ConsoleError(
                    "no uploads directory at '{}' use -f to create".format(args.uploads)
                )

        for dataset in args.datasets:
            # Remove the trailing slash
            dataset = dataset.rstrip(os.path.sep)

            # Check if the dataset is valid
            if not args.force and not is_valid(dataset, False):
                print(color.format("cannot package invalid dataset at {}", color.LIGHT_RED, dataset))
                continue

            name = os.path.basename(dataset)
            out = os.path.join(args.uploads, name)

            if not args.force and os.path.exists(out+".zip"):
                print(color.format("dataset exists at {} use -f to overwrite", color.LIGHT_YELLOW, out))
                continue

            try:
                out = shutil.make_archive(out, "zip", root_dir=os.path.dirname(dataset), base_dir=name)
                self.update_manifest(out)
            except Exception as e:
                print(color.format("could not package dataset {} at {}: {}", color.LIGHT_RED, dataset, out.rstrip(".zip")+".zip", e))
                continue

            print(color.format("packaged dataset at {}", color.LIGHT_GREEN, out))

    def update_manifest(self, dst):
        """
        Update the JSON manifest with the package data and hash.
        """
        # Read the current manifest into memory
        mpath = os.path.join(os.path.dirname(dst), "manifest.json")
        try:
            with open(mpath, 'r') as f:
                manifest = json.load(f)
        except IOError:
            manifest = {}

        name, _ = os.path.splitext(os.path.basename(dst))
        # Update the manifest record
        manifest[name] = {
            "url": os.path.basename(dst),
            "signature": sha256sum(dst),
        }

        # Write the manifest back to disk
        with open(mpath, 'w') as f:
            json.dump(manifest, f, indent=2)