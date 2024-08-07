# Opentender data exploration

The aim of this repository is to fetch data from opentenders.eu, load and clean it and in a jupyter notebook explore it.
Running
    ```python3 src/main.py --help```
gives description of usage. At present form it can load one country with specified years to a dataframe, or explore this data in a jupyter notebook.

Description of the columns of the used data can be found at `data/DIGIWHIST_CSV_descriptions_180530.pdf`

## Issues
Fetching by a spider or programmatically data from opentender.eu did not work out. You can find `src/opentender_scraper` and `src.utils.download_procurement_data` as my trials. 
opentender.eu does not provide public API access, thus I had to mock the `post` HTTP method, which did not prove to e successful. To avoid wasting too much time on this issue I continued by
assuming the `csv` files are placed in `data/` folder. A solution would have been using a web browser automation framework like `selenuim` but I think that is not exactly interesting for this case study.

## Install requirements

The dependencies and virtual environment are managed by poetry.
On global Python scope or the used virtualenv in the project you need to install `poetry` by 
    ```pip3 install poetry```

After that, installing dependencies:
    ```poetry install```

## Formatting code base

Code formatting is done by `black`

    ```black src```

## Data exploration
Data exploration is utilizing the data loading and exploring the dataframes in a jupyter notebook. Start the notebook like:
    ```jupyter notebook```

Select the file `notebooks/data-exploration.ipynb`

## Further development
- [] error handling, tests
- [] data fetching from opentender.eu
- [] adding docstrings
- [] sphynx documentation generation based on docstrings
- [] instead of local data persistence have a cloud based backend for the cleaned data
- [] more insightful statistics and plots