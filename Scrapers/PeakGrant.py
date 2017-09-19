#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as BS
import json
import datetime

# Main publications
entries = 1
outfile = open("../Data/PeakGrant_Upload.json","w")
url1 = "https://www.peakgrantmaking.org/publications/"
page = requests.get(url1)
parsed = BS(page.content, 'html.parser')
content = parsed.find('div',id="content-full")
articles = content.find_all('td')
for entry in articles:
    title = entry.find('h3')
    if title:
        outfile.write('{"index":{"_id":"'+str(entries)+'"}}\n{')
        outfile.write('"Source_Title": "'+title.get_text().replace('\n','')+'"')
        notes = entry.find_all('p')
        description = ''.join(i.get_text() for i in notes).replace('\n','')
        outfile.write(', "Description": "'+description+'"')
        outfile.write(', "Source_Type": "Publication"')
        outfile.write(', "datafromresource": "peakgrantmakingorg"')
        outfile.write('}\n')
        entries += 1
    else:
        continue
outfile.close()

# Archived publications
entries2 = 1
outfile2 = open("../Data/PeakGrant_Archived_Upload.json","w")
url2 = "https://www.peakgrantmaking.org/about/news/archived-publications/"
page2 = requests.get(url2)
parsed2 = BS(page2.content, 'html.parser')
titles2 = parsed2.find_all('h3')
for i in range(0,len(titles2)):
    outfile2.write('{"index":{"_id":"'+str(entries2)+'"}}\n{')
    title2 = titles2[i].get_text().replace('\n','')
    outfile2.write('"Source_Title": "'+title2+'"')
    description2 = titles2[i].next_sibling.get_text().replace('\n','')
    outfile2.write(', "Description": "'+description2+'"')
    outfile2.write(', "Source_Type": "Publication"')
    outfile2.write(', "datafromresource": "peakgrantmakingorg"')
    outfile2.write('}\n')
    entries2 += 1
outfile2.close()
