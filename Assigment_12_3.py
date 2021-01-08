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

# Getting inputs:
url = input("Enter URL: ")
if url == "":
    url = "http://py4e-data.dr-chuck.net/known_by_Meghana.html"

count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Spider through the links:
print("Retrieving: ", url)

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    line_number = 0

    for tag in tags:
        line_number += 1
        if line_number != position:
            continue
        else:
            url = tag['href']
            print("Retrieving: ", url)
            name = tag.contents[0]

print(name)
