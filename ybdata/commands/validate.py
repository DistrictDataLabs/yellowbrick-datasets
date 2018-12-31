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

CHECKMARK  = color.format(u"✓", color.LIGHT_GREEN)
CROSSMARK  = color.format(u"✗", color.LIGHT_RED)


##########################################################################
## Command
##########################################################################

class ValidateCommand(Command):

    name = "validate"
    help = "validates a dataset's readiness for upload"
    args = {}

    def handle(self, args):
        """
        Run the dataset through each checker and print out a checklist table.
        """
        print("hi")