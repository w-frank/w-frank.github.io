#!/bin/sh

git add .
git commit -m "$1"
git push -u origin pelican
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master -m "$1"
git push -u origin master
git checkout pelican
