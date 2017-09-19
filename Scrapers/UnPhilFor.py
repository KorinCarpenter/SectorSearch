#!/usr/bin/python3

import requests
import re
from bs4 import BeautifulSoup as BS
import json
import datetime

entries = 1
pagenumber = 0
outfile = open("../Data/UnPhilFor_Upload.json","w")
while True:
    page = requests.get("https://www.unitedphilforum.org/resources/search?keys=&page="+str(pagenumber))
    parsed = BS(page.content, 'html.parser')

    title = parsed.find_all('h2',class_="node-title")
    content = parsed.find_all('div',class_="content clearfix")
    for entry in range(0,len(title)):
        outfile.write('{"index":{"_id":"'+str(entries)+'"}}\n')
        outfile.write('{"Source_Title": "'+title[entry].get_text()+'"')
        corrected_entry = entry + 4
        publication_date = ""
        final_date = ""
        date = content[corrected_entry].find('span',class_="date-display-single")
        if date:
            publication_date = date.get_text()
            final_date = datetime.datetime.strptime(publication_date, '%M/%Y').strftime('%Y-%M')
            outfile.write(', "publicationDate": "'+final_date+'"')
        description = content[corrected_entry].find('div',class_="field field-name-body field-type-text-with-summary field-label-hidden")
        if description:
            outfile.write(', "Description": "'+description.get_text()+'"')
        audience = content[corrected_entry].find_all('a',href=re.compile("/audience/"))
        audiences = []
        if audience:
            for i in range(0,len(audience)):
                audiences.append(audience[i].get_text())
            outfile.write(', "Population": '+json.dumps(audiences))
        resource_type = content[corrected_entry].find_all('a',href=re.compile("/resource-type/"))
        resource_types = []
        if resource_type:
            for i in range(0,len(resource_type)):
                resource_types.append(resource_type[i].get_text())
            outfile.write(', "Source_Type": '+json.dumps(resource_types))
        topic = content[corrected_entry].find_all('a',href=re.compile("/topic/"))
        topics = []
        if topic:
            for i in range(0,len(topic)):
                topics.append(topic[i].get_text())
            outfile.write(', "Subject_Issue": '+json.dumps(topics))
        outfile.write(', "datafromresource": "unitedphilforumorg"')
        outfile.write('}\n')
        entries += 1
    if not(parsed.find_all('li',class_="pager-next")):
        break
    pagenumber += 1
outfile.close()
