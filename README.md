# VedaWeb TEI transformations

This repository contains the files employed to transform the [source files](https://github.com/VedaWebProject/vedaweb-data) of the VedaWeb project into the [TEI format](https://github.com/VedaWebProject/vedaweb-data/tree/main/rigveda/TEI) and validate them.

Requirements: [conda](https://conda-forge.org/download/)

After installing conda, follow these steps to transform and validate the data

1. Create the virtual environment and install the needed dependencies:\
   `conda env create -f environment.yml`
2. Activate the virtual environment:\
   `conda activate vedaweb_transformations`
3. Clone the vedaweb-data repository\
   `git clone https://github.com/VedaWebProject/vedaweb-data.git`
4. Transform the source data to TEI\
   `python transform.py <path_to_vedaweb-data> <path_to_vedaweb-data/rigveda/TEI>`\
   (The second argument is the path to the output directory)
5. Validate the generated TEI files\
   `python validate.py <path_to_vedaweb-data/rigveda/TEI>`
6. Deactivate the virtual environment when you are done\
   `conda deactivate`


## Development

If you want to apply changes (installed/uninstalled depenencies) in the environment to the `environment.yml`, run...

```
conda env export --from-history --channel conda-forge > environment.yml
```

**Important:** After doing this, delete the line starting with `prefix: ...` from the `environment.yml`!


## Upcoming Updates
There will be a code and TEI update in 2025.
