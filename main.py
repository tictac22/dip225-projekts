import sys
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv
from months import sheet_title
from salary import get_salary

load_dotenv()

salary = get_salary()

def stop_program():
    sys.exit() 

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID =  os.environ.get("SPREADSHEET_ID")

creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
# Save the credentials for the next run
with open("token.json", "w",encoding="utf-8") as token:
    token.write(creds.to_json())

if not creds:
    sys.exit()

service = build("sheets", "v4", credentials=creds)
request = {
    "requests": [
        {
            "addSheet": {
                "properties": {
                    "title": sheet_title 
                }
            }
        }
    ]
}

service.spreadsheets().batchUpdate(body=request,spreadsheetId=SPREADSHEET_ID).execute()


days = [ i for i in range(1,32)]
titles = ["Pārtikas", "Transports", "Pakalpojumi", "Apģērbs"]
titles.append(None)
titles.append("Total total:")
titles.extend(titles[:-1])

request = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {
            "range": f"{sheet_title}!A6:A36",
            "majorDimension": "COLUMNS",
            "values": [
                days
            ]
        },
        {
            "range": f"{sheet_title}!B5:K5",
            "majorDimension": "ROWS",
            "values": [
                titles
            ]
        },
        {
            "range": f"{sheet_title}!H7:K7",
            "majorDimension": "ROWS",
            "values": [
                ["=SUM(B6:B36)","=SUM(C6:C36)","=SUM(D6:D36)","=SUM(E6:E36)"]
            ]
        },
        {
            "range": f"{sheet_title}!G13:I13",
            "majorDimension": "ROWS",
            "values": [
                ["Ienākums",'Izdevumi',"Starpība"]
            ]
        },
        {
            "range": f"{sheet_title}!G14:I14",
            "majorDimension": "ROWS",
            "values": [
                [salary,'=SUM(H7:K7)',"=G14-H14"]
            ]
        },
    ]
}
service.spreadsheets().values().batchUpdate(body=request,spreadsheetId=SPREADSHEET_ID).execute()


row_data = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,range="A4:Z4").execute()
existing_values = row_data.get('values', [])
row_length = len(existing_values[0]) if existing_values else 0
next_letter = chr(ord("A") + row_length)
request = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {
            "range": f"Total Chart!{next_letter}3:{next_letter}6",
            "majorDimension": "COLUMNS",
            "values": [
                [sheet_title,f"='{sheet_title}'!G14",f"='{sheet_title}'!H14"]
            ]
        },
    ]
}
service.spreadsheets().values().batchUpdate(body=request,spreadsheetId=SPREADSHEET_ID).execute()