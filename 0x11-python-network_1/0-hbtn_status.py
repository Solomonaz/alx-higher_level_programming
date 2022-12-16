#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status.
"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        response = res.read()
    print("Body response:")
    print("     - type: ", type(response))
    print("     - content: ", response)
    print("     - utf8 content: ", response.decode('utf-8'))
