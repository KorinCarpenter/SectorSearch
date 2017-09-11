#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as BS
import json
import datetime

entries = 1
pagenumber = 1
outfile = open("../Data/Chicago/UploadData.json","w")
while True:
    page = requests.get("https://data.cityofchicago.org/browse?&page="+str(pagenumber))
    parsed = BS(page.content, 'html.parser')
    content = parsed.find_all('div',class_="browse2-result")
    for entry in content:
        outfile.write('{"index":{"_id":"'+str(entries)+'"}}\n{')
        title = entry.find('a',class_="browse2-result-name-link")
        outfile.write('"Source_Title": "'+title.get_text()+'"')
        issue = entry.find('a',class_="browse2-result-category browse2-result-header-section")
        if issue:
            outfile.write(', "Subject_Issue": "'+issue.span.get_text()+'"')
        keywords = entry.find_all('a',class_="browse2-result-topic")
        words = []
        if keywords:
            for word in keywords:
                words.append(word.get_text())
            outfile.write(', "Keywords": '+json.dumps(words))
        sourcetype = entry.find('div',class_="browse2-result-type")
        if sourcetype:
            outfile.write(', "Source_Type": "'+sourcetype.find('span',class_="browse2-result-type-name").get_text()+'"')
        description = entry.find('div',class_="browse2-result-description")
        if description:
            notestoprint = description.get_text().replace('"','').replace('(','').replace(')','').replace('&','and').replace('\n','')
            outfile.write(', "Description": "'+notestoprint+'"')
        date = entry.find('div',class_="browse2-result-timestamp-value")
        if date:
            publication_date = date.span.get_text()
            final_date = datetime.datetime.strptime(publication_date, '%B %d %Y').strftime('%Y-%m-%d')
            outfile.write(', "publicationDate": "'+final_date+'"')
        outfile.write(', "datafromresource": "datacityofchicagoorg"')
        outfile.write(', "Geographic_Focus": "Chicago"')
        outfile.write('}\n')
        entries += 1
    if not(parsed.find_all('a',class_="next nextLink browse2-pagination-button")):
        break
    pagenumber += 1
outfile.close()
