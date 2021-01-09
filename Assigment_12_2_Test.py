# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://kiszamolo.hu/penzugyi-tanacsadas/"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
count = 0
p_tags = soup('p')
for p_tag in p_tags:
    if count < 1:
        count += 1
        print('<p> TAG:', p_tag)
        print('Contents:', p_tag.contents[0])
        print('Attrs value:', p_tag.get('class', None))
        print('Attrs key-value:', p_tag.attrs, "\n")
    else:
        break

count = 0
a_tags = soup('a')
for a_tag in a_tags:
    if count < 1:
        count += 1
        print('<a> TAG:', a_tag)
        print('Contents:', a_tag.contents[0])
        print('Attrs value:', a_tag.get('href', None))
        print('Attrs key-value:', a_tag.attrs, "\n")
    else:
        break

#Print count and sum up:
print("Count ", count)
print(type(soup))
print(type(p_tags))
