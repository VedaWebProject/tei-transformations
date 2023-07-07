# c-salt_vedaweb_transformations

This repository contains the files employed to transform the [source files](https://github.com/VedaWebProject/vedaweb-data) of the VedaWeb project in [TEI format](https://github.com/VedaWebProject/vedaweb-data/tree/main/rigveda/TEI) and validate them.

Requirements: [conda](https://docs.conda.io/en/latest/miniconda.html)

After installing conda, you should import the `environment.yml` file and, activate it.


## Transform

`python transform.py (path_to_vedaweb-data/rigveda) (output_path)`


## Validate

`python validate.py (path_to_vedaweb-data/rigveda/TEI)`
