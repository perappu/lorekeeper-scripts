#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Error: No argument provided."
  exit 1
fi

cd ~/$1/www/

php artisan migrate --force

php artisan add-site-settings

php artisan optimize:clear

php artisan optimize