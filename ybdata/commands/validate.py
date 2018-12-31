# ybdata.commands.validate
# Validates a dataset checking if its ready for upload.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 07:32:02 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: validate.py [] benjamin@bengfort.com $

"""
Validates a dataset checking if its ready for upload.
"""

##########################################################################
## Imports
##########################################################################

from commis import color, Command
from tabulate import tabulate

from ybdata.validate import standard_package_checklist, is_valid_standard
from ybdata.validate import corpus_package_checklist, is_valid_corpus

CHECKMARK  = color.format(u"✓", color.LIGHT_GREEN)
CROSSMARK  = color.format(u"✗", color.LIGHT_RED)


##########################################################################
## Command
##########################################################################

class ValidateCommand(Command):

    name = "validate"
    help = "validates a dataset's readiness for upload"
    args = {
        ("-t", "--type"): {
            "choices": {"standard", "corpus"}, "default": "standard",
            "help": "type of dataset to validate against",
        },
        ("-O", "--exclude-optional"): {
            "action": "store_true", "default": False,
            "help": "exclude optional checklist criteria",
        },
        "dataset": {
            "type": str, "nargs": 1, "metavar": "PATH",
            "help": "path(s) to datasets to validate",
        }
    }

    def handle(self, args):
        """
        Run the dataset through each checker and print out a checklist table.
        """
        if args.type == "standard":
            checklist = standard_package_checklist(args.dataset[0], not args.exclude_optional)
            valid = is_valid_standard(args.dataset[0], False)
        elif args.type == "corpus":
            checklist = corpus_package_checklist(args.dataset[0], not args.exclude_optional)
            valid = is_valid_corpus(args.dataset[0], False)
        else:
            raise ValueError("did not understand type '{}'".format(args.type))

        table = [["", args.dataset[0]]]
        for item, checked in checklist.items():
            table.append([CHECKMARK if checked else CROSSMARK, item])

        print(tabulate(table, tablefmt="simple", headers="firstrow"))
        valid_msg, valid_color = {
            True: ("is valid and ready to be uploaded", color.LIGHT_GREEN),
            False: ("needs additional requirements before upload", color.LIGHT_RED),
        }[valid]
        print(color.format("\n{} {}", valid_color, args.dataset[0], valid_msg))