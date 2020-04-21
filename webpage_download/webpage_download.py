import requests
import wget
from bs4 import BeautifulSoup

print(wget.__file__)
# This is the url you should edit based on the files you want to download
url = 'https://rawdata.oceanobservatories.org/files/CP01CNSM/R00011/cg_data/dcl12/pco2a'
ext = 'log'

def listFD(url, extension=''):
    page = requests.get(url).text
    #print(page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(extension)]

fileList = []
for file in listFD(url, ext):
    fileList.append(file)

for file in fileList:
    fileName = file.rsplit('/', 1)[-1]
    wget.download(file)