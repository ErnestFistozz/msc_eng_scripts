#! /usr/local/bin/bash

codecov_repo_dir="CodeCovRepositories"
coveralls_repo_dir="CoverallsRepositories"
mkdir -p $codecov_repo_dir

codecov_repos=(`ls java-repos-csv/*.csv`)
coveralls_repos=(`ls coveralls-repos-cvs/*csv`)

cd $codecov_repo_dir
for repo in "${codecov_repos[@]}"
do
    
    git clone git@github.com:apache/$repo.git
done