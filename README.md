# Yellowbrick Datasets
**Yellowbrick datasets management and deployment scripts.**

Yellowbrick datasets are hosted in an S3 drive in the cloud to allow easy access to the data for examples. This repository manages those datasets, their data structure, and interactions with the cloud.

## Getting Started

The `ybdata` script is installed as an entry point in `setup.py`. You can install the package and the script using `pip install yellowbrick-data`. If you've downloaded the source code from GitHub you can install the app using editable mode with pip. In the current working directory of the project, use:

```
$ pip install -e .
```

At this point you should have a `ybdata` command on your `$PATH`. Like git, this utility has many subcommands for various data related management tasks. To see a list of the commands and their descriptions:

```
$ ybdata --help
```

## Datasets Basics

All datasets must have the following properties:

- a unique name that identifies the dataset to a user (e.g. "bikeshare")
- a README.md that describes the provenance and contents of the data
- one or more data files that can be read by the yellowbrick library
- an optional citation.bib file to cite the source of the data

Datasets are stored in the `fixtures/` directory in a subdirectory with the same name as the dataset. This subdirectory contains both the data and metadata files that make up the data package structure. The `uploads/` directory contains the most recent version of the compressed datasets found in the `fixtures/` directory and is the content that is uploaded to S3 for use in Yellowbrick.

Currently there are two kinds of datasets:

1. Standard: A single data table containing both features and targets.
2. Corpus: A text corpus for natural language processing.

Both kinds of datasets have their own specific package structures as defined in the following sections. Note that the `ybdata validate` command can be used to check if a dataset is ready to be uploaded.

### Standard Datasets

A standard dataset is composed of a single data table that can be loaded into a data frame or numpy array for machine learning with scikit-learn. In addition to the files mentioned in dataset basics, the data and metadata files that make up the standard dataset package are as follows (where "name" is the unique dataset name):

- `fixtures/name/name.csv.gz`: The gzip compressed CSV file _with header row_ to be loaded with `pd.read_csv` (no index column).
- `fixtures/name/name.npz`: The compressed numpy matrix representation of `X` and `y` to be loaded with `np.load`.
- `fixtures/name/meta.json`: A metadata file that identifies the features and the target column names of the data in the CSV file.

Consider the following example CSV file:

```csv
datetime,temperature,relative humidity,light,CO2,humidity,occupancy
2015-02-04 17:51:00,23.18,27.272,426,721.25,0.00479298817650529,1
2015-02-04 17:51:59,23.15,27.2675,429.5,714,0.00478344094931065,1
2015-02-04 17:53:00,23.15,27.245,426,713.5,0.00477946352442199,1
2015-02-04 17:54:00,23.15,27.2,426,708.25,0.00477150882608175,1
2015-02-04 17:55:00,23.1,27.2,426,704.5,0.00475699293331518,1
2015-02-04 17:55:59,23.1,27.2,419,701,0.00475699293331518,1
2015-02-04 17:57:00,23.1,27.2,419,701.666666666667,0.00475699293331518,1
2015-02-04 17:57:59,23.1,27.2,419,699,0.00475699293331518,1
2015-02-04 17:58:59,23.1,27.2,419,689.333333333333,0.00475699293331518,1
```

An example `meta.json` for this file would be as follows:

```json
{
  "features": [
      "temperature",
      "relative humidity",
      "light",
      "CO2",
      "humidity",
  ],
  "target": "occupancy",
  "labels": {
    "occupied": 1,
    "not occupied": 0
  }
}
```

This will ensure that the dataset `X` is a `pd.DataFrame` with columns corresponding to the features list and that `y` is a `pd.Series` from the column described in the `target` key. The `labels` key is used to transform numerically encoded categorical variables for a classification target.

### Corpus Datasets

A corpus dataset contains plain text files stored in subdirectories of the dataset directory that correspond to the class or category the plain text files belong to. Note that these text files should be only one level deep and that each document should be stored in its own file.

At the momement, individual corpus files should be uncompressed (the directory as a whole is compressed). The text corpus is read similarly to the following:

```python
import os
import glob

paths = os.path.join(data_dir, "*", "*.txt")
documents = glob.glob(paths)
labels = [os.path.basename(os.path.dirname(path)) for path in documents]
```

Documents and labels can then be directly passed to scikit-learn text feature extraction transformers for analysis.

## Uploading Datasets

## Creating Datasets

This section to be completed in more detail.

Most of the datasets in this repository are from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). Until this section is completed, I recommend looking at one of the datasets as an example to see how to transform the data from the source repository to one that Yellowbrick can make direct use of.