import urllib.request, urllib.parse, urllib.error
import json
import ssl

# API:
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create URL:
address = input('Enter location: ')

parms = dict()
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

# Retrieving URL:
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
raw_data = uh.read().decode()
print('Retrieved', len(raw_data), 'characters')

# Convert webpage to JSON data:
try:
    json_data = json.loads(raw_data)
except:
    json_data = None

if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(raw_data)

# Convert JSON data to Python data to pretty print it:
print(json.dumps(json_data, indent=4))

# Extract place id:
place_id = json_data['results'][0]['place_id']

print("Place id:\n", place_id)
print(len(json_data["results"][0]))