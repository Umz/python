#   Soup.py Using Beautiful Soup to access HTML via DOM

import bs4

#   CREATE a DOM object from data

ex = open('ex.html')
noSS = bs4.BeautifulSoup(ex.read(), features="html.parser")

elems = noSS.select('#p1')
p1 = elems[0]

print (p1.getText())
print (p1.attrs)
