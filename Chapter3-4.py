from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Get the internal link list
def getInternalLinks(bsObj, includeUrl): # includeUrl is the include Url address which should be appeared in the internal link
    internalLinks = []
    for link in bsObj.findAll("a", href = re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# Get the external link list
def getExternalLinks(bsObj, excludeUrl): # excludeUrl is the exclude Url address which should be absent in the external link
    externalLinks = []
    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        # If there ain't any external links appeared in the page, then randomly pick a internal link of the page,
        # search for the external link in this child page.
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://www.oreilly.com")
    print("Random External Link is: " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://www.oreilly.com")

# allExtLinks = set()
# allIntLinks = set()
# def getAllExternalLinks(siteUrl):
#     html = urlopen(siteUrl)
#     bsObj = BeautifulSoup(html)
#     internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
#     externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
#     for link in externalLinks:
#         if link not in allExtLinks:
#             allExtLinks.add(link)
#             print(link)
#     for link in internalLinks:
#         if link not in allIntLinks:
#             print("The present URL is: " + link)
#             allIntLinks.add(link)
#             getAllExternalLinks(link)
#
# getAllExternalLinks("http://www.oreilly.com")

