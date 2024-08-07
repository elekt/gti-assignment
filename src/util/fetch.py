import datetime
import logging
import os.path

import requests
import pandas as pd
import zipfile
from typing import List

ZIP_FOLDER = os.path.join(os.getcwd(), f"data")
ZIP_EXTRACT_FOLDER = os.path.join(os.getcwd(), "data/extracted")


def download_procurement_data(cc: str):
    # URL = f"https://opentender.eu/data/downloads/data-{cc}-csv.zip"

    URL = f"https://opentender.eu/data/downloads/data-{cc}-csv.zip"

    with requests.Session() as s:
        payload = {
            "name": "Tamas Elekes",
            "organization": "None",
            "email": "elekestamas22@gmail.com",
            "sector": "NGO",
            "send_info_about_product": False,
            "datasets_download": ["LT"],
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Referer": "https://opentender.eu/",  # Change to your referer if necessary
            "Content-Type": "application/json",
            "Referrer Policy": "strict-origin-when-cross-origin",
        }

        result = s.post(URL, json=payload, headers=headers, allow_redirects=True)
        # result = s.get(URL)

        decoded_content = result.content.decode("utf-8")
        pass


def unzip_downloaded_data(cc: str):
    zip_location = os.path.join(ZIP_FOLDER, f"data-{cc}-csv.zip")
    with zipfile.ZipFile(zip_location, "r") as zip_ref:
        zip_ref.extractall(os.path.join(ZIP_EXTRACT_FOLDER, cc))


def load_data_to_pandas(cc: str, years: List[int]) -> pd.DataFrame:
    cc_location = os.path.join(ZIP_EXTRACT_FOLDER, cc)
    expected_files = [f"data-{cc}-{year}.csv" for year in years]
    files = [file for file in os.listdir(cc_location) if file in expected_files]

    if len(expected_files) != len(files):
        logging.warning(
            f"Not all requested years could be loaded. Fetch data if needed. Found files: {files}"
        )

    dfs = []

    dateparse = lambda x: datetime.datetime.strptime(x, "%Y-%m-%d")
    date_cols = [
        "tender_publications_firstCallForTenderDate",
        "tender_publications_lastCallForTenderDate",
        "tender_publications_firstdContractAwardDate",
        "tender_publications_lastContractAwardDate",
    ]
    for file in files:
        df = pd.read_csv(
            os.path.join(cc_location, file),
            sep=";",
            header=0,
            low_memory=False,
            parse_dates=date_cols,
            date_format=dateparse,
        )
        df[date_cols] = df[date_cols].apply(pd.to_datetime, format="%Y-%m-%d")
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)

    return df
