from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

# ######################### Urlopen a URL #############################
# try:
#     html = urlopen("http://pythonscraping.com/pages/page1.html")
#
# # If the page is not existed.
# except HTTPError as e:
#     print(e)
#     # Another action if needed
# # else:
#     # Action if needed
#
# # If the server is not existed.
# if html is None:
#     print("URL is not found")
# # else:
#     # Program goes ahead
#
# ######################## URL open completed#########################
# bsObj = BeautifulSoup(html.read())
#
# try:
#     badContent
# print(bsObj.nonExisting.someTag)

######################## Functions ################################
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
