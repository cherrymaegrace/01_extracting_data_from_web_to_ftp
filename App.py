import sys
import json
import time
import schedule
import pandas as pd
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

# This function returns an authenticated FTP where the extracted data will be uploaded in.
def get_ftp() -> FTP_TLS:

    ftphost = environ["FTPHOST"]
    ftpuser = environ["FTPUSER"]
    ftppassword = environ["FTPPASSWORD"]

    # Login to FTP
    ftp = FTP_TLS(ftphost, ftpuser, ftppassword)

    # Set up secure data connection
    ftp.prot_p()
    print("Successfully connected to FTP.")

    return ftp

def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]

    return pd.read_csv(url, **params)

def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as fp:
        ftp.cwd('./ftp/new')
        ftp.storbinary(f"STOR {file_source.name}", fp)

def delete_csv(file_source: str | Path):
    remove(file_source)

def pipeline():
# Load source config
    with open("config.json","rb") as fp:
        config = json.load(fp)

    # Loop through each source file in the config and download each file
    for source_file_name, source_file_config in config.items():
        file_name = Path(source_file_name + ".CSV")
        csv_file = read_csv(source_file_config)

        csv_file.to_csv(file_name, index=False)
        print(f"Successfully downloaded {file_name}.")

        # Get authenticated FTP
        ftp = get_ftp()

        # Upload source files
        upload_to_ftp(ftp, file_name)
        print(f"Successfully uploaded {file_name}.")

        # Delete files
        delete_csv(file_name)
        print(f"Successfully deleted {file_name}.")

if __name__ == "__main__":

    # Option for scheduling pipeline run
    run_manual = sys.argv[1];

    if run_manual.lower() == "true":
        pipeline()

    elif run_manual.lower() == "false":
        schedule.every().day.at("23:00").do(pipeline())

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid parameter. The app will not run.")
    