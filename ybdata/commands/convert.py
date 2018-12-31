# ybdata.commands.convert
# Convert dataset into required formats.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Dec 31 10:34:22 2018 -0500
#
# For license information, see LICENSE.txt
#
# ID: convert.py [] benjamin@bengfort.com $

"""
Convert dataset into required formats.
"""

##########################################################################
## Imports
##########################################################################

import os
import json

import numpy as np
import pandas as pd

from commis import color, Command
from commis.exceptions import ConsoleError


VALID_EXTS = {".csv", ".csv.gz", ".npz"}

##########################################################################
## Command
##########################################################################

class ConvertCommand(Command):

    name = "convert"
    help = "convert dataset into required format"
    args = {
        "src": {
            "type": str, "metavar": "src",
            "help": "path to dataset source file to convert",
        },
        "dst": {
            "type": str, "metavar": "dst",
            "help": "path to write converted dataset to",
        }
    }

    def handle(self, args):
        """
        Convert the dataset from one format to another.
        """
        stype = self.get_data_type(args.src)
        dtype = self.get_data_type(args.dst)

        if stype not in VALID_EXTS:
            print(color.format("Unknown source type '{}'", color.LIGHT_RED, stype))
            return

        if dtype not in VALID_EXTS:
            print(color.format("Unknown convert type '{}'", color.LIGHT_RED, dtype))
            return

        # Load source data
        if stype.startswith(".csv"):
            # Load data with pandas
            X, y = self.load_pandas(args.src)
        elif stype == ".npz":
            # Load data with numpy
            data = np.load(args.src)
            X, y = data.get("X"), data.get("y")
        else:
            raise NotImplementedError("conversion from {} to {} not implemented yet".format(stype, dtype))

        # Perform the conversion and save
        if dtype == ".npz":
            # Save as numpy compressed
            np.savez_compressed(args.dst, X=X, y=y)
        elif dtype.startswith(".csv"):
            # Save as pandas data frame
            df = pd.concat([pd.DataFrame(X), pd.Series(y)], axis=1)
            meta = self.load_meta(args.src)
            header = meta['features'] + [meta['target']]
            compression = "gzip" if dtype.endswith(".gz") else None
            df.to_csv(args.dst, index=False, header=header, compression=compression)
        else:
            raise NotImplementedError("conversion from {} to {} not implemented yet".format(stype, dtype))

    def load_meta(self, path):
        """
        Load metadata from meta.json in the same directory as the source
        """
        meta_path = os.path.join(os.path.dirname(path), "meta.json")

        try:
            with open(meta_path, 'r') as f:
               meta = json.load(f)
        except Exception as e:
            raise ConsoleError(
                "could not load required metadata from '{}': {}".format(meta_path, e)
            )

        if "features" not in meta or "target" not in meta:
            raise ConsoleError("meta.json is missing required information")

        return meta

    def load_pandas(self, path):
        """
        Convert a pandas data frame into X, y for saving to numpy
        """
        meta = self.load_meta(path)
        compression = "gzip" if path.endswith(".gz") else None
        data = pd.read_csv(path, compression=compression)
        return data[meta["features"]], data[meta["target"]]

    def get_data_type(self, path):
        """
        Like os.path.splitext but keeps all dot extensions after dirname.
        """
        name = os.path.basename(path)
        parts = name.split(".")
        return "." + ".".join(parts[1:])