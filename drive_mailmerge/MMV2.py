#!  python3
#   MMV2.py
#   Mail Merge V2. Using the Sample for the Read Document title to try and build
#   mail merge application. The MM sample failed on credentials and every alternative

from __future__ import print_function

import time
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#   ITERABLE (Delete tocken.json when modifying scopes)

SCOPES = (
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
)

#   IDs of the docs

DOC_ID = '1UhCwvgGbNpQpZB_4rjdhHawX0tjgSRiYDGHCX4V0Mmo'
SHEET_ID = "1cfbsag1WGsJlnv29sqWEUkEvk8Qz8tkQx4B-wz8w9fo"

#   FUNCTIONS defined below

def _copy_template(doc, service):
    """
    (private) COPIES letter template using Drive API and return file ID of copy
    """
    try:
        body = {'name':'Merged Letter (sheet)'}
        return service.files().copy(body=body, fileId=doc, fields='id').execute().get('id')
    except HttpError as error:
        print(f"An error occured {error}")
        return error

def merge_template(document, service, DOCS, data):
    """
    COPIES template Doc and merge data into new copy then return file ID
    """
    try:
        #   COPY template and set context data struct for merging template values
        copyId = _copy_template(document, service)
        context = data.iteritems() if hasattr({}, 'iteritems') else data.items()

        #   SEARCH & REPLACE API requests for mail merge substitutions
        reqs = [{'replaceAllText' : {
            'containsText': {
                'text': '{{%s}}' % key,
                'matchCase': False
            },
            'replaceText': value
        }} for key, value in context]

        #   SEND request to Google Docs API to do the actual merge
        DOCS.documents().batchUpdate(body={'requests':reqs}, documentId=copyId, fields='').execute()
        return copyId

    except HttpError as error:
        print(f"An error occured {error}")
        return error

#   MAIN flow below

def main():
    """
    AUTHORIZE the user to access Drive, Docs and Sheets with Permissions
    Grab the Document and Sheet for the Merge
    Merge the Sheet into the Docs and save the merged documents in drive
    """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'g-auth.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:

        DRIVE = build('drive', 'v2', credentials=creds)
        DOCS = build('docs', 'v1', credentials=creds)
        SHEETS = build('sheets', 'v4', credentials=creds)

        #   KEYS to be replaced in document

        COLUMNS = ['ID', 'Name', 'Address']
        keys = {
            'ID': None,
            'Name': None,
            'Address': None
        }

        #   GET sheet data (Skips the header row)

        rows = SHEETS.spreadsheets().values().get(spreadsheetId=SHEET_ID, range='Sheet1').execute().get('values')[1:];

        for i, row in enumerate(rows):

            #   UPDATE the dictionary each iteration for the merge

            keys.update(dict(zip(COLUMNS, row)))
            newID = merge_template(DOC_ID, DRIVE, DOCS, keys)
            print ('Merged letter %d: docs.google.com/document/d/%s/edit' % (i + 1, newID))

            #   RENAME the new file

            try:

                file = DRIVE.files().get(fileId=newID)
                copyName = "MMT_%s" % keys['Name']
                DRIVE.files().update(fileId=newID, body={'title':copyName}).execute()
            except HttpError as error:
                print(f"An error occured {error}")
                return error

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
