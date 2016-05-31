import requests

params = {'email_addr': 'ryan.e.mitchell@gmall.com'}
r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data = params)
print(r.text)