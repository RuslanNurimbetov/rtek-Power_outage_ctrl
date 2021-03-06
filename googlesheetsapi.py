"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint
import RPi.GPIO as GPIO
import time
from googleapiclient import discovery

GPIO.setmode(GPIO.BCM)
GPIO.setup(8,GPIO.IN)
GPIO.setup(10,GPIO.IN)
GPIO.setup(14,GPIO.IN)
GPIO.setup(16,GPIO.IN)


x0 = GPIO.input(8)
x1 = GPIO.input(10)
x2 = GPIO.input(14)
x3 = GPIO.input(16)


# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'
credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to update.
spreadsheet_id = 'Power_outage_log'  # TODO: Update placeholder value.

# The A1 notation of a range to search for a logical table of data.
# Values will be appended after the last row of the table.
range_ = 'my-range'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = ''  # TODO: Update placeholder value.

# How the input data should be inserted.
insert_data_option = ''  # TODO: Update placeholder value.

value_range_body = {
    # TODO: Add desired entries to the request body.
}

request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
