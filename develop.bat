pelican -s pelicanconf.py -o output content
cd output
python -m http.server
cd ..
