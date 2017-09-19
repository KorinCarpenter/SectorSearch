#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as BS
import json
import datetime

topics = ["advocacy-lobbying","boards-governance","ceo-leadership-development","development-gift-management","disaster-grantmaking-0","diversity-inclusion","donor-advised-funds","ethics-accountability","expenditure-responsibility","financial-management","foundation-lifecycle","foundation-management","funds-management","global-grantmaking","grants-management","impact-investing-0","investment-spending-policies","marketing-communications","nonmonetary-grants","partnerships-collaboration","grants-individuals","self-dealing","tax-filing-audits"]
for topic in topics:
    entries = 1
    filename = "../Data/CounFound_"+topic.replace('-','')+"_Upload.json"
    outfile = open(filename,"w")
    pagenumber = 0
    while True:
        url = "https://www.cof.org/topic/"+topic+"?page="+str(pagenumber)
        page = requests.get(url)
        parsed = BS(page.content, 'html.parser')
        content = parsed.find_all('article')
        for entry in content:
            outfile.write('{"index":{"_id":"'+str(entries)+'"}}\n{')
            title = entry.find('h3')
            outfile.write('"Source_Title": "'+title.get_text().replace('\n','')+'"')
            issue = topic.replace('-',' ').title()
            outfile.write(', "Subject_Issue": "'+issue+'"')
            info_type = entry.find('div',class_="topics")
            keywords = info_type.get_text().replace('G','Getting Started').replace('W','Working Knowledge').replace('A','Advanced Knowledge').replace('L','Legal Compliance').replace('M','Members Only').split('\n')
            keywords = list(filter(None,keywords))
            outfile.write(', "Keywords": '+json.dumps(keywords))
            description = entry.find('div',class_="field-content")
            if description:
                outfile.write(', "Description": "'+description.get_text().replace('"','').replace('\n','')+'"')
            outfile.write(', "datafromresource": "councilonfoundationsorg"')
            item_url = "https://www.cof.org"+str(title.get('href'))
            outfile.write(', "URL": "'+item_url+'"')
            outfile.write('}\n')
            entries += 1
        if not(parsed.find_all('li',class_="next")):
            break
        pagenumber += 1
    outfile.close()
