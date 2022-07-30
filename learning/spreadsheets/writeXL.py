#!  python3
#   CREATING and saving spreadsheets

import openpyxl

wb = openpyxl.Workbook()
wb.sheetnames

sheet = wb.active

sheet.title = 'Created Sheet';

wb.save('ex.xlsx')
