# Extracting Data from the Web to FTP using Python

This project is an output of the __[Episode 03](https://www.youtube.com/watch?v=j7fNG-V4aGE&t=5649s)__ of Josh Dev's Building Your First End-to-End Data Portfolio series.

## Output Overview
This output showcases the creation of a data pipeline that extracts data from an online source and uploads the extracted files to an SFTP server.

## Learning Outcomes:
- Set-up an FTP Server on WSL (Windows Subsystem for Linux)
- Create a Python virtual environment and store FTP credentials as environment variables
- Secure successful connection to an FTP Server in Python
- Extract .CSV files from an online source
- Upload extracted files to an FTP Server
- Schedule a data pipeline

## Datasets
The following datasets from __[OFAC Consolidated List](https://sanctionslist.ofac.treas.gov/Home/ConsolidatedList)__ were used:
- CONS_PRIM.CSV
- CONS_ADD.CSV
- CONS_ALT.CSV