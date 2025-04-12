import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import random
from utils import enforce_gender_rule, enter_data , capitalize_first_letter, quiz

# Path to the JSON file with the service account credentials
creds_file = r"D:\coding\VocabNote\credentials\vocabnote-425819-9e3b675a3e5a.json"

# Define the scope
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Authenticate with the service account
creds = Credentials.from_service_account_file(creds_file, scopes=scope)

# Connect to Google Sheets
client = gspread.authorize(creds)

# Open the Google Sheet by title
sheet = client.open('German words and meanings').sheet1

# Read data from the sheet
data = sheet.get_all_records()
#print(data)

df = pd.DataFrame(data)
#df.head(10)


##MAIN FUNCTION
if __name__ == "__main__":
    choice=int(input("what do u want to do 1. enter data, 2. quiz"))

    if choice==1:
        enter_data(sheet)
    else:
        num_questions = int(input("Enter the number of questions: ").strip())
        quiz(data, num_questions=num_questions)