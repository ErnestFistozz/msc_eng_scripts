#!/usr/bin/bash

scc_languages="py,java,js,mjs,jsp,hh,hpp,hxx,inl,ipp,cc,cpp,cxx,pcc,mm,go,groovy,grt,gtpl,gvy,m,pl,pm,php,rb,erb,rhtml,sc,scala,swift,ts,tsx,vue"
cloc_languages="Java,Scala,Perl,Python,Swift,Julia,CSharp,Go,Groovy,JavaScript,Kotlin,TypeScript,Ruby,C++"

csv_path=$1
filename=$2

while IFS=, read -r timestamp Commit CodeCoverage
do
    if [ -z "$Commit" ]; 
    then 
        echo "empty hash"
    else
        echo "starting"
        git checkout $Commit
        echo "done checking out"
        cloc_loc=$(cloc --include-lang=$cloc_languages . | grep -i SUM | awk '{ print $5 }')
        scc_loc=$(scc -i $scc_languages --no-cocomo . | grep -i Total | awk '{ print $6 }')
        scc_complexity=$(scc -i $scc_languages --no-cocomo . | grep -i Total | awk '{ print $7 }')
        echo "$cloc_loc, $scc_loc, $scc_complexity" >> $csv_path/$filename.txt
        echo "done"
    fi
done < <(tail -n +2 $csv_path/$filename.csv)

exit 0