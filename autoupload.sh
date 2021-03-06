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
        curl -sS -XPOST ${URL} --data-binary @${upfile}
        sleep 15
    fi
done | sed 's/{"index":/\n{"index":/g' | sed 's/{"took":/\n{"took":/g' | awk '{ if (/\"status\":400/) { print > "Logs/error.log" } else { print > "Logs/success.log" } }'
# > /dev/null 2>&1

