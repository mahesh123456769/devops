import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope for accessing Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using the credentials.json (downloaded from Google Cloud Console)
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet by its name
spreadsheet = client.open("Your Google Sheet Name").sheet1  # Replace with the name of your Google Sheet

# To read the entire sheet
data = spreadsheet.get_all_records()  # Returns list of dictionaries (rows)

# To write data to the sheet (e.g., inserting a new row with responses)
row = ["John Doe", "john.doe@example.com", "25"]  # Example form data
spreadsheet.append_row(row)

print("Data written to Google Sheet:")
print(row)
