#!/bin/sh

pelican -s pelicanconf.py -o output content
cd output
python3 -m http.server
cd ..
