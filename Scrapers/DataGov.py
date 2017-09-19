#!/usr/bin/env python

import requests
import json


errors = []
start = 0
while start < 198000:
    block = str(start)
    start = start + 1000
    URL = "https://catalog.data.gov/api/3/action/package_search?rows=1000&start=" + block

    # send GET request
    rsp = requests.get(URL)
    fileName = "../Data/DataGov_" + block + "_Scraped.json"
    # check response status code
    if (rsp.status_code == 200):
        jsonData = rsp.json()
        with open(fileName,'w') as outfile:
            json.dump(jsonData, outfile)
            outfile.close()
    else:
        errorinfo = "Something went wrong with the " + block + " block"
        errors = errors.append(errorinfo)
        #raise Exception("Bad status code")
        continue
