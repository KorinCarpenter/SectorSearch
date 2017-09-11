#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as BS
import datetime
import json

index = 1
outfile = open("LGBTFunders.json","w")
page = requests.get("https://www.lgbtfunders.org/research/",verify=False)
parsed = BS(page.content, 'html.parser')
content = parsed.find_all('div',class_="col-md-3 col-sm-6")
for page in content:
    results = page.a.get('href')
    url = "https://www.lgbtfunders.org"+results
    result = requests.get(url,verify=False)
    parsed_result = BS(result.content,'html.parser')
    result_content = parsed_result.find('div',class_="col-md-9")
    outfile.write('{"index":{"_id":"'+str(index)+'"}}\n')
    title = result_content.find('h1')
    outfile.write('{"Source_Title": "'+title.get_text()+'"')
    date = result_content.contents[3]
    if date:
        publication_date = str(date)
        final_date = datetime.datetime.strptime(publication_date,' %m/%d/%Y').strftime('%Y-%m-%d')
        outfile.write(', "publicationDate": "'+final_date+'"')
    author = result_content.contents[6]
    author_list = []
    if author:
        authors = str(author)
        author_list = authors.split(',')
        outfile.write(', "Source_Author": '+json.dumps(author_list)+'')
    notes = result_content.find_all('p')
    description = ""
    if notes:
        for paragraph in notes:
            description += paragraph.get_text()
        outfile.write(', "Description": "'+description+'"')
    organization = result_content.find('h4')
    if organization:
        outfile.write(', "Organization": "'+organization.get_text()+'"')
    outfile.write(', "Population": "LGBTQ"')
    outfile.write(', "datafromresource": "lgbtfundersorg"')
    outfile.write('}\n')
    index += 1
outfile.close()
