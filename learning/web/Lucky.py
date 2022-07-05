#!  python3
#   Lucky.py - Search Google and open first results on page

import requests, sys, webbrowser, bs4

search = sys.argv[1:]

print ('Googling... %s' % (' '.join(search)))       #   Display while downloading results page
res = requests.get('http://google.com/search?q=' + ' '.join(search))
res.raise_for_status()

#   Retrieve top search results on the page
#   TODO:   Find a way to sift through the relevant <a> tags

soup = bs4.BeautifulSoup(res.text, features="html.parser")
results = [];

elems = soup.select('.BNeawe a')
for e in elems:
    #print (e.parent)
    results.append(e.get('href'))

unique = set(results)
links = list(unique)
toOpen = min(5, len(links))

#   OPEN a browser tab for each link

for i in range(toOpen):
    webbrowser.open('http://google.com/' + links[i])
