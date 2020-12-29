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

# Spider through the links:
count = int(input("Enter count: "))
position = int(input("Enter position: "))

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

for i in range(count+1):
    print("Retrieving: ", url)
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    name = tags[position].contents[0]
    line_number = 0

    for tag in tags:
        line_number += 1
        if line_number != position:
            continue
        else:
            url = tag['href']
