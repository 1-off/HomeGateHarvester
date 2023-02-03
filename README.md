# HomeGateHarvester
Collect and analyze large amounts of data from Homegate.ch.

## Description
Python scripts that imports data from a CSV file to a Google Sheet. The script uses the gspread library to interact with the Google Sheets API and the oauth2client library for authentication. The script first authenticates to the API by loading the credentials from a JSON file and then creates a connection to the Google Sheet. The data from the CSV file is then read, and the headers and rows are appended to the Google Sheet. The script prints a message indicating that the data has been successfully written to the Google Sheet.

