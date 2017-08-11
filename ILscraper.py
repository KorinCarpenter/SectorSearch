#!/usr/bin/env python

import requests
import json
import sys
from email.mime.text import MIMEText

# construct base url
API_key = "10c3051cf5923c348355d7b33ac638bc54509bf7"
Issues = ["Aging","Agriculture and Food","Animal Welfare","Arts and Culture","Athletics and Sports","Children and Youth","Civil Society","Community and Economic Development","Computers and Technology","Consumer Protection","Crime and Safety","Disabilities","Education and Literacy","Employment and Labor","Energy and Environment","LGBTQI","Government Reform","Health","Housing and Homelessness","Humanitarian and Disaster Relief","Human Rights and Civil Liberties","Hunger","Immigration","International Development","Journalism and Media","Men","Nonprofits and Philanthropy","Parenting and Families","Peace and Conflict","Poverty","Prison and Judicial Reform","Race and Ethnicity","Religion","Science","Substance Abuse and Recovery","Transportation","Welfare and Public Assistance","Women"]
errors = []
for issue in Issues:
    URL = "http://data.issuelab.org/fetch/key/" + API_key + "/format/json/issues/" + issue

    # send GET request
    rsp = requests.get(URL)
    filename = issue.replace(" ","")
    # check response status code
    if (rsp.status_code == 200):
        jsonData = rsp.json()
        jsonFileName = "./IssueLabFiles/" + filename + ".json"
        with open(jsonFileName,'w') as outfile:
            json.dump(jsonData, outfile)
    else:
        errorinfo = "Something went wrong with " + issue
        errors = errors.append(errorinfo)
        #raise Exception("Bad status code")
        continue

