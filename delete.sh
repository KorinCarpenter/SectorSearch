#!/bin/bash

echo "Which indices would you like to delete?"
read indices

for i in $indices
do
    index=$(echo $i | awk '{print tolower($0)}')
    curl -sS -XDELETE 'https://search-sectorsearch-7xx3kcc77prfjydwdcmxftyoni.us-east-1.es.amazonaws.com/'$index
done

