# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() # The read() returns the entire webpage as a huge string (with newlines at the end of each line) instead of an iterable filehandle
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a') #Gives back a list of <a> </a> tags.
for tag in tags:
    print(tag.get('href', None)) # Prints the content of the "href"attribute in the <a> tags
