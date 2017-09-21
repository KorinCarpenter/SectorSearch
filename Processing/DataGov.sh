#!/bin/bash

count=1
for ((i=0;i<198000;i+=1000))
do
  infile='../Data/DataGov_'$i'_Scraped.json'
  outfile='../Data/DataGov_'$i'_Upload.json'
  sed 's/.*results": \[//' $infile > Step$i.json

  ./DataGov.pl Step$i.json > temp$i.json

  sed -e '$ d' temp$i.json |
  sed 's/"notes"/"Description"/g' |
  sed 's/"maintainer"/"Source_Author"/g' |
  sed 's/"type":/"Source_Type":/g' |
  sed 's/"format":/"Source_Format":/g' |
  sed 's/"metadata_create":/"publicationDate":/g' |
  sed 's/"title":/"Source_Title":/g' |
  sed 's/"\[{/\[{/g' |
  sed 's/}\]"/}\]/g' |

  while read line
    do
      printf "{\"index\":{\"_id\":\"%s\"}}\n" "$count"
      printf "%s\n" "$line"
      ((count++))
  done > $outfile
done
rm Step* temp* ../Data/DataGov_*_Scraped.json
