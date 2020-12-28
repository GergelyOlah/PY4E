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

def parser(url, pos, cnt):
    print(url)
    repeat = cnt - 1
    if repeat = 1
        next_url = None
    else:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        line_number = 0
    
        for tag in tags:
            line_number += 1
            if line_number != pos:
                continue
            else:
                next_url = tag['href']
                parser(next_url,pos,repeat)

        return next_url

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
line_number = 0
#for tag in tags:
    #print(tag.get('href', None))
    #print(tag['href'])


#count = int(input("Enter count: "))
#position = int(input("Enter position: "))

#parser("http://py4e-data.dr-chuck.net/known_by_Fikret.html", position)
  