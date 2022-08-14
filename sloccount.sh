#! /usr/local/bin/bash

repo_dir="/Users/admin/Desktop/MSc-Repos"
scripts_dir=msc_eng_scripts
codecov=java-repos-csv
coveralls=coveralls-repos-
filename=$1
scc_languages="py,java,js,mjs,jsp,hh,hpp,hxx,inl,ipp,cc,cpp,cxx,pcc,mm,go,groovy,grt,gtpl,gvy,m,pl,pm,php,rb,erb,rhtml,sc,scala,swift,ts,tsx,vue"
cloc_languages="Java,Scala,Perl,Python,Swift,Julia,CSharp,Go,Groovy,JavaScript,Kotlin,TypeScript,Ruby,C++"

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
        #loc=$(cloc . | grep -i sum | awk '{ print $5 }')
        #sloccount_loc=$(sloccount . | grep -i "Total Physical Source Lines of Code (SLOC)" | awk '{ print $9 }')
        cloc_loc=$(cloc --include-lang=$cloc_languages . | grep -i SUM | awk '{ print $5 }')
        scc_loc=$(scc -i $scc_languages --no-cocomo . | grep -i Total | awk '{ print $6 }')
        scc_complexity=$(scc -i $scc_languages --no-cocomo . | grep -i Total | awk '{ print $7 }')
        echo "$cloc_loc, $scc_loc, $scc_complexity" >> $repo_dir/$scripts_dir/$codecov/$filename.txt
        echo "done"
    fi
done < <(tail -n +2 $repo_dir/$scripts_dir/$codecov/$filename.csv)

exit 0