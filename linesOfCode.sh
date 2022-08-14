#! /usr/local/bin/bash

repo_dir="/Users/admin/Desktop/MSc-Repos"
scripts_dir=msc_eng_scripts
codecov=java-repos-csv
coveralls=coveralls-repos-
filename=$1

cd "$repo_dir/$filename";

while IFS=, read -r timestamp Commit CodeCoverage
do
    if [ -z "$Commit" ]; 
    then 
        echo "empty hash"
    else
        echo "starting"
        git checkout $Commit
        echo "done checking out"
        #loc=$(git summary --line | grep -i lines | awk '{ print $3 }')
        loc=$(cloc . | grep -i sum | awk '{ print $5 }')
        echo $loc >> $repo_dir/$scripts_dir/$codecov/$filename.txt
        echo "done"
    fi
done < <(tail -n +2 $repo_dir/$scripts_dir/$codecov/$filename.csv)

exit 0