#!/bin/bash

declare -a sources=("centeffphil" "

declare -a issues=("Aging" "AgricultureandFood" "AnimalWelfare" "ArtsandCulture" "AthleticsandSports" "ChildrenandYouth" "CivilSociety" "CommunityandEconomicDevelopment" "ComputersandTechnology" \
"ConsumerProtection" "CrimeandSafety" "Disabilities" "EducationandLiteracy" "EmploymentandLabor" "EnergyandEnvironment" "GovernmentReform" "Health" "HousingandHomelessness" "HumanRightsandCivilLiberties" \
"HumanitarianandDisasterRelief" "Hunger" "Immigration" "InternationalDevelopment" "JournalismandMedia" "Men" "NonprofitsandPhilanthropy" "ParentingandFamilies" "PeaceandConflict" "Poverty" \
"PrisonandJudicialReform" "RaceandEthnicity" "Religion" "Science" "SubstanceAbuseandRecovery" "Transportation" "WelfareandPublicAssistance" "Women")
for i in "${issues[@]}"
do
    echo $i
done
