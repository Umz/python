#!  python3
#   MailMerge.py -  USING Python to merge Google Doc with Google Sheet
#   There is no native way to do this for some reason?

from __future__ import print_function

import time
import os

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#   DOCUMENT template ID and Data Sources (Docs and Sheets)

#   AUTH CONSTANTS

SCOPES = (  # ITERABLE or space-delimited string
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
)

#   APP CONSTANTS

#SOURCE = 'sheets'
COLUMNS = ['ID', 'First Name', 'Address']

SOURCE = 'text'
TEXT_SOURCE = (
    (101, 'Tester 1', '123 Test Lane, TT1 1TE'),
    (102, 'Tester 2', '123 Test Lane, TT1 2TE')
)

creds, _ = google.auth.default()
# pylint =

#   SERVICE endpoints to Google APIs

DRIVE = build('drive', 'v2', credentials=creds)
DOCS = build('docs', 'v1', credentials=creds)
SHEETS = build('sheets', 'v4', credentials=creds)

#   FUNCTION def

def get_data(source):
    """
    GRAB the mail merge data from the given data source
    """
    try:
        return SAFE_DISPATCH[source]()
    except HttpError as error:
        print(f"An error has occured: {error}")
        return error

def _get_text_data():
    """
    (private) Return plain text data; can alter to read from CSV instead
    """
    return TEXT_SOURCE

def _get_sheets_data(services=SHEETS):
    """
    (private) Returns data from Google Sheets source. It gets all rows of 'Sheet1'
    (default sheet in a new Spreadsheet) but drops the first (header) row. Use any
    desired data range (in standard A1 notation)
    """
    #   SKIP the header row [1:]
    return service.spreadsheets().values().get(spreadsheetId=SHEET_ID, range='Sheet1').execute().get('values')[1:]

#   DATA source dispatch
SAFE_DISPATCH = {k: globals().get('_get_%s_data' % k) for k in SOURCES}

def _copy_template(temId, source, service):
    """
    (private) COPIES letter template using Drive API and return file ID of copy
    """
    try:
        body = {'name':'Merged Letter (%s)' % source}
        return service.files().copy(body=body, fileId=temId, fields='id').execute().get('id')
    except HttpError as error:
        print(f"An error occured {error}")
        return error

def _merge_template(temId, source, service):
    """
    COPIES template Doc and merge data into new copy then return file ID
    """
    try:
        #   COPY template and set context data struct for merging template values
        copyId = _copy_template(temId, source, service)
        context = merge.iteritems() if hasattr({}, 'iteritems') else merge.items()

        #   SEARCH & REPLACE API requests for mail merge substitutions
        reqs = [{'replaceAllText' : {
            'containsText': {
                'text': '{{%s}}' % key
            },
            replaceText: value
        }} for key, value in context]

        #   SEND request to Google Docs API to do the actual merge
        DOCS.documents().batchUpdate(body={'requests':reqs}, documentId=copyId, fields='').execute()
        return copyId

    except HttpError as error:
        print(f"An error occured {error}")
        return error

if __name__ == '__main__':

    #   FILL in data to merge into document

    merge = {
        #   RECIPIENT data (supplied by SOURCE)
        'ref': None,
        'name': None,
        'address': None
    }

    data = get_data(SOURCE)     #   GET data from source

    for i, row in enumerate(data):
        merge.update(dict(zip(COLUMNS, row)))
        print ('Merged letter %d: docs.google.com/document/d/%s/edit' % (i + 1, merge_template(DOC_ID, SOURCE, DRIVE)))
