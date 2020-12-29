import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Getting inputs:
""" url = input("Enter URL: ")
if url == "": """
url = "http://py4e-data.dr-chuck.net/comments_42.xml"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xml = urllib.request.urlopen(url, context=ctx)
data = xml.read()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
sums = 0
count = 0

for tag in results:
    count += 1
    number = int(tag.find("count").text)
    sums += number

print(count, sums)




