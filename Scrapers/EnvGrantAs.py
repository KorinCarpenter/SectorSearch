#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as BS
import json
import datetime

entries = 1
pagenumber = 0
outfile = open("../Data/EnvGrantAs/UploadData.json","w")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
while True:
    url = "https://ega.org/learn/publications?page="+str(pagenumber)
    page = requests.get(url,headers=headers)
    parsed = BS(page.content, 'html.parser')
    titles = parsed.find_all('div',class_="views-field-title")
    dates = parsed.find_all('span',class_="date-display-single")
    descriptions = parsed.find_all('div',class_="field-content")
    for entry in range(0,len(titles)):
        outfile.write('{"index":{"_id":"'+str(entries)+'"}}\n{')
        title = titles[entry].get_text().replace('\n','')
        outfile.write('"Source_Title": "'+title+'"')
        outfile.write(', "Subject_Issue": "Environment"')
        outfile.write(', "Source_Type": "Publication"')
        description = descriptions[entry].get_text().replace('\n','')
        outfile.write(', "Description": "'+description+'"')
        date = dates[entry].get_text()
        final_date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
        outfile.write(', "publicationDate": "'+final_date+'"')
        outfile.write(', "datafromresource": "environmentalgrantmakersassociationorg"')
        outfile.write('}\n')
        entries += 1
    if not(parsed.find_all('li',class_="pager-next")):
        break
    pagenumber += 1
outfile.close()
