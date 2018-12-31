# ybdata.commands.list
# List the datasets already uploaded to S3
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 16:54:36 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: list.py [] benjamin@bengfort.com $

"""
List the datasets already uploaded to S3
"""

##########################################################################
## Imports
##########################################################################

import boto3

from commis import Command
from .upload import BUCKET

from ybdata.utils import urljoin


##########################################################################
## Command
##########################################################################

class ListCommand(Command):

    name = "list"
    help = "list datasets uploaded to s3"
    args = {
        ("-b", "--bucket"): {
            "default": BUCKET, "help": "s3 bucket to upload data to",
        },
        ("-p", "--prefix"): {
            "default": "", "help": "specify a key prefix to filter on",
        },
        ("-s", "--suffix"): {
            "default": "", "help": "specify a key suffix to filter on",
        }
    }

    def handle(self, args):
        s3 = boto3.client("s3")

        kwargs = {'Bucket': args.bucket, 'Prefix': urljoin('yellowbrick', args.prefix)}
        while True:
            resp = s3.list_objects_v2(**kwargs)
            for obj in resp['Contents']:
                if obj['Key'].endswith(args.suffix):
                    print(obj['Key'])

            try:
                kwargs['ContinuationToken'] = resp['NextContinuationToken']
            except KeyError:
                break