#   Reqs.py Getting files and data by scraping

import requests

#   GET web page

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status()
except Exception as e:
    raise Exception('There was a problem: %s' % (e))

#   WRITE content to file

playFile = open('RomeoJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

print ('File finished downloading')
