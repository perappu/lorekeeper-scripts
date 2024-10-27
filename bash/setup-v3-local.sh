#!/bin/bash

git clone https://github.com/corowne/lorekeeper.git --branch release/v3.0.0 $1

cd $1

git branch -m main

git remote rename origin lorekeeper

git remote add site $2

git remote add origin $3

# add common extension sources
git remote add ext-CH3RVB-lorekeeper-tweaks https://github.com/CH3RVB/lorekeeper-tweaks.git

git remote add ext-AW0005 https://github.com/AW0005/lorekeeper-extensions.git

git remote add ext-DeeP-ci https://github.com/DeeP-ci/lorekeeper.git

git remote add ext-JuniJwi https://github.com/JuniJwi/lorekeeper.git

git remote add ext-MarskyMessier https://github.com/MarskyMessier/lorekeeper.git

git remote add ext-AnimatedCritter https://github.com/AnimatedCritter/lorekeeper.git 

git remote add ext-CH3RVB https://github.com/CH3RVB/lorekeeper.git

git remote add ext-Cylunny https://github.com/Cylunny/lorekeeper.git

git remote add ext-itinerare https://github.com/itinerare/lorekeeper.git

git remote add ext-lumephobia https://github.com/lumephobia/lorekeeper.git

git remote add ext-perappu https://github.com/perappu/lorekeeper.git

git remote add ext-preimpression https://github.com/preimpression/lorekeeper.git

git remote add ext-Draginraptor https://github.com/Draginraptor/lorekeeper.git

git remote add ext-ScuffedNewt https://github.com/ScuffedNewt/lorekeeper.git

git push origin main