import argparse
import datetime
import logging

import os
print(os.getcwd())
from src.util.fetch import (
    unzip_downloaded_data,
    download_procurement_data,
    load_data_to_pandas,
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="GTI-assignment",
        description="Opentender data parser, can download, clean and analyse a european countries pulic procurement data.",
    )
    parser.add_argument(
        "cc", help="Country code of the analysed European country in ISO 3166 format"
    )

    parser.add_argument(
        "-y",
        "--years",
        nargs="+",
        help="<Optional> Years of data to load, if omitted, current year will be loaded",
        default=[datetime.datetime.now().strftime('%Y')]
    )

    parser.add_argument(
        "-d",
        "--debug",
        help="<Optional> Show debug logs",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="<Optional> Show verbose logs",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )

    args = parser.parse_args()

    # SETUP LOGGING
    logging.basicConfig(
        format="%(levelname)s:%(name)s:%(message)s", level=args.loglevel
    )

    # download_procurement_data(args.cc)
    unzip_downloaded_data(args.cc)

    df = load_data_to_pandas(args.cc, args.years)

    print(df.head())
