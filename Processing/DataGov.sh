#!/bin/bash

count=1
for ((i=172000;i<198000;i+=1000))
do
  infile='./DataGovFiles/DataGov_'$i'.json'
  outfile='./CleanedFiles/DataGov_'$i'.json'
  sed 's/.*results": \[//' $infile > Step$i.json
  
  ./DGperlprocess.pl Step$i.json > temp$i.json
  
  sed -e '$ d' temp$i.json | 
  sed 's/"notes"/"Description"/g' | 
  sed 's/"maintainer"/"Source_Author"/g' | 
  sed 's/"type":/"Source_Type":/g' |
  sed 's/"format":/"Source_Format":/g' | 
  sed 's/"metadata_create":/"publicationDate":/g' | 
  sed 's/"title":/"Source_Title":/g' | 
  
  while read line
    do
      printf "{\"index\":{\"_id\":\"%s\"}}\n" "$count"
      printf "%s\n" "$line"
      ((count++))
  done > $outfile
done
rm Step* temp*
