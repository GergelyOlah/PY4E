import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Getting inputs:
url = input("Enter URL: ")
if url == "":
    url = "http://py4e-data.dr-chuck.net/comments_1131337.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retriving URL:
print("Retrieving", url)
json_page = urllib.request.urlopen(url, context=ctx)
raw_data = json_page.read().decode() #"bytes" data is decoded to "string"

# Turning JSON to Python data structure:
json_data = json.loads(raw_data)
print("Retrieved {} characters".format(len(raw_data)))
print("Raw data type:\n", type(raw_data))
print("Json data type:\n", type(json_data))

# Parsing through the list and extract the text:
sums = 0
count = 0

for user in json_data["comments"]:
    count += 1
    sums += int(user["count"])
    
print("Count: ", count)
print("Sum: ", sums)