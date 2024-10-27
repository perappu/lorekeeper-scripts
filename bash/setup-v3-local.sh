#!/bin/bash

git clone https://github.com/corowne/lorekeeper.git release/v3.0.0 .

git branch -m main

git remote rename origin lorekeeper

git remote add $1 site

git remote add $2 origin

# add common extension sources


git push origin main