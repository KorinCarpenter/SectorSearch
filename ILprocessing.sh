#!/bin/bash

declare -a arr=("Aging" "AgricultureandFood" "AnimalWelfare" "ArtsandCulture" "AthleticsandSports" "ChildrenandYouth" "CivilSociety" "CommunityandEconomicDevelopment" "ComputersandTechnology" "ConsumerProtection" "CrimeandSafety" "Disabilities" "EducationandLiteracy" "EmploymentandLabor" "EnergyandEnvironment" "GovernmentReform" "Health" "HousingandHomelessness" "HumanRightsandCivilLiberties" "HumanitarianandDisasterRelief" "Hunger" "Immigration" "InternationalDevelopment" "JournalismandMedia" "Men" "NonprofitsandPhilanthropy" "ParentingandFamilies" "PeaceandConflict" "Poverty" "PrisonandJudicialReform" "RaceandEthnicity" "Religion" "Science" "SubstanceAbuseandRecovery" "Transportation" "WelfareandPublicAssistance" "Women")


for i in "${arr[@]}"
do
  infile='./IssueLabFiles/'$i'.json'
  outfile='./CleanedFiles/'$i'.json'
  count=1
  sed 's/^.\{15\}//' $infile |
  sed -e $'s/}, /}\\\n/g' |
  sed 's/"publication_date":/"publicationDate":/g' | 
  sed 's/"issues":/"Subject_Issue":/g' | 
  sed 's/"pubtypes":/"Source_Type":/g' | 
  sed 's/"authors":/"Source_Author":/g' | 
  sed 's/"description":/"Description":/g' | 
  sed 's/"title":/"Source_Title":/g' | 
  
  {
    while read line
    do
      printf "{\"index\":{\"_id\":\"%s\"}}\n" "$count"
      printf "%s\n" "$line"
      ((count++))
    done
  } > $outfile
done
