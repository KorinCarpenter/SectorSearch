#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as BS
import json
import datetime

entries = 1
pagenumber = 1
outfile = open("../Data/GeoFund_Upload.json","w")
while True:
    url = "https://www.geofunders.org/resources?page="+str(pagenumber)
    page = requests.get(url)
    parsed = BS(page.content, 'html.parser')
    content = parsed.find_all('li',class_="TeaserListing-item")
    for entry in content:
        outfile.write('{"index":{"_id":"'+str(entries)+'"}}\n{')
        title = entry.find('p',class_="Teaser-title f-stag").get_text().replace('\n','').strip()
        outfile.write('"Source_Title": "'+title+'"')
        sourcetype = entry.find('span',class_="Teaser-label")
        if sourcetype:
            outfile.write(', "Source_Type": "'+sourcetype.get_text()+'"')
        keywords = entry.find('span',class_="Teaser-label Teaser-label--pill")
        if keywords:
            outfile.write(', "Keywords": ["'+keywords.get_text()+'"]')
        notes = entry.find('div',class_="Teaser-summary f-stag-sans-light")
        if notes:
            description = notes.get_text().replace('\n','').strip()
            outfile.write(', "Description": "'+description+'"')
        info = entry.find_all('li',class_="Teaser-meta-item f-stag-sans-light")
        if info:
            date = info[0].get_text()
            final_date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
            outfile.write(', "publicationDate": "'+final_date+'"')
            if len(info)>1:
                author = info[1].get_text()
                outfile.write(', "Source_Author": "'+author+'"')
        outfile.write(', "datafromresource": "geofundersorg"')
        outfile.write('}\n')
        entries += 1
    if not(parsed.find_all('li',class_="Pagination-item Pagination-item--next")):
        break
    pagenumber += 1
outfile.close()
