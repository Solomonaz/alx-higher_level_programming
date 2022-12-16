#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    response = res.read()
print("Body response:")
print("     - type: ", type(response))
print("     - content: ", response)
print("     - utf8 content: ", response.decode('utf-8'))
