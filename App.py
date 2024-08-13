import os
from ftplib import FTP_TLS

# This function returns an authenticated FTP where the extracted data will be uploaded in.
def get_ftp() -> FTP_TLS:

    # Login to FTP
    ftp = FTP_TLS()

    ftphost = os.environ["FTPHOST"]
    ftpuser = os.environ["FTPUSER"]
    ftppassword = os.environ["FTPPASSWORD"]

    ftp.connect(ftphost)
    ftp.login(ftpuser, ftppassword)

    # Set up secure data connection
    ftp.prot_p
    print("Successfully connected to FTP.")

    return ftp

if __name__ == "__main__":
    get_ftp()