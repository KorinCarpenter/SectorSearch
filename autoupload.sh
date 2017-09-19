#!/bin/bash

ScrapedFiles="$(ls Data/)"
UploadURL="https://search-sectorsearch-7xx3kcc77prfjydwdcmxftyoni.us-east-1.es.amazonaws.com"

for s in $ScrapedFiles
do
    i="$(basename $s .json)"
    upload="$(echo ${i} | awk -F_ '{print $NF}')"
    if [ "${upload}" == "Upload" ]; then
        index="$(echo ${i} | awk -F_ '{print $1}')"
        topic="$(echo ${i} | awk -F_ '{print $2}')"
        if [ "${topic}" == "Upload" ]; then
            topic="data"
        fi
        upinfo="${index}/${topic}"
        URLAddition="$(echo ${upinfo} | awk '{print tolower($0)}')"
        URL="${UploadURL}/${URLAddition}/_bulk"
        upfile="./Data/$s"
        curl -XPOST ${URL} --data-binary @${upfile}
    fi
done > /dev/null 2>&1

