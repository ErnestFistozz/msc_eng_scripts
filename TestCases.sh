#!/usr/local/bin/bash

#code_base_dir=$1
project_name=$1


cd "/Users/admin/Desktop/MSc-Repos/${project_name}";

while IFS=, read -r timestamp Commit CodeCoverage
do
    if [ -z "$Commit" ]; then
        echo "Empty Hash"
    else
        git checkout $Commit
        file_paths=()
        while IFS= read -r -d $'\0'; do
            file_paths+=("$REPLY")
        done < <(find . -name '*Test*.java' -print0)
        no_of_test_cases=0
        for file in "${file_paths[@]}"; do
            case_count=$(cat $file | grep -i '@Test' | wc -l)
            ((no_of_test_cases=no_of_test_cases+$case_count))
        done
        echo $no_of_test_cases >> "/Users/admin/Desktop/MSc-Repos/msc_eng_scripts/${project_name}_TestCases".txt
    fi

done < <(tail -n +1 /Users/admin/Desktop/MSc-Repos/msc_eng_scripts/java-repos-csv/"${project_name}.csv")





