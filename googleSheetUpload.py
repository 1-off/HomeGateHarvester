# Import the required libraries
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the function for converting the csv file to Google Sheets
def csv_to_sheet(file_path):
    # Authenticate to the Google Sheets API using the provided service account credentials
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet named "houses"
    sheet = client.open("houses").sheet1

    # Read the data from the CSV file
    with open(file_path, 'r') as file:
        # Create a csv reader object
        reader = csv.reader(file)
        
        # Get the headers from the first row of the csv file
        headers = next(reader)

        # Write the headers to the first row of the Google Sheet
        sheet.append_row(headers)

        # Loop through the remaining rows of the csv file and write each row to the Google Sheet
        for row in reader:
            sheet.append_row(row)

    # Print a success message once the data has been written to the Google Sheet
    print("Data from the CSV file has been successfully written to Google Sheets!")
