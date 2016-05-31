import requests

params = {'username' : 'Ryan', 'passwd' : 'passwd'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print('Cookie is set to: ')
print(r.cookies.get_dict())
print("--------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies = r.cookies)

