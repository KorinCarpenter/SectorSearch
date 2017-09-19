#!/bin/bash

UploadFiles="$(ls ~/SectorSearch/Data | basename _Upload.json | awk '{print tolower($0)}' | grep -v .json)"
UploadURL="https://search-sectorsearch-7xx3kcc77prfjydwdcmxftyoni.us-east-1.es.amazonaws.com"

for s in $UploadFiles
do
    echo $s
#    i="$(basename $s _Upload.json)"
#    uploadfile="$(echo ${i} | awk '{print tolower($0)}' | grep -v .json)"
#    echo ${UploadURL}"/"${uploadfile}
done


#declare -a issues=("Aging" "AgricultureandFood" "AnimalWelfare" "ArtsandCulture" "AthleticsandSports" "ChildrenandYouth" "CivilSociety" "CommunityandEconomicDevelopment" "ComputersandTechnology" \
#"ConsumerProtection" "CrimeandSafety" "Disabilities" "EducationandLiteracy" "EmploymentandLabor" "EnergyandEnvironment" "GovernmentReform" "Health" "HousingandHomelessness" "HumanRightsandCivilLiberties" \
#"HumanitarianandDisasterRelief" "Hunger" "Immigration" "InternationalDevelopment" "JournalismandMedia" "Men" "NonprofitsandPhilanthropy" "ParentingandFamilies" "PeaceandConflict" "Poverty" \
#"PrisonandJudicialReform" "RaceandEthnicity" "Religion" "Science" "SubstanceAbuseandRecovery" "Transportation" "WelfareandPublicAssistance" "Women")
#for i in "${issues[@]}"
#do
#    echo $i
#done
