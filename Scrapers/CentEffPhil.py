#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as BS
import datetime
import json

index = 1
outfile = open("~/SectorSearch/Data/CentEffPhil/UploadData.json","w")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
page = requests.get("http://efphilanthropy.wpengine.com/research/publications/",headers=headers)
parsed = BS(page.content, 'html.parser')
content = parsed.find_all('a',class_="w-portfolio-item-anchor")
for page in content:
    results = page.get('href')
    url = results
    result = requests.get(url,headers=headers)
    parsed_result = BS(result.content,'html.parser')
    result_content = parsed_result.find('div',class_="span12 widget-span widget-type-widget_container ")
    if not(result_content):
        continue
    outfile.write('{"index":{"_id":"'+str(index)+'"}}\n')
    title = parsed_result.find('h1')
    outfile.write('{"Source_Title": "'+title.get_text()+'"')
    date = result_content.find_all('strong')
    if date:
        publication_date = date[-1].get_text()
        final_date = datetime.datetime.strptime(publication_date,'%B %Y').strftime('%Y-%m')
        outfile.write(', "publicationDate": "'+final_date+'"')
    notes = result_content.find_all('p')
    description = ""
    if notes:
        for paragraph in notes:
            if paragraph.find('strong'):
                continue
            description += paragraph.get_text()
        outfile.write(', "Description": "'+description.replace('\n','')+'"')
    outfile.write(', "Organization": "Center for Effective Philanthropy"')
    outfile.write(', "URL": "'+url+'"')
    outfile.write(', "datafromresource": "centerforeffectivephilanthropyorg"')
    outfile.write('}\n')
    index += 1
outfile.close()
