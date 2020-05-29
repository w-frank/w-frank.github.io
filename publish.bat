git add .
git commit -a -m %1
git push -u --force origin pelican
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master -m %1
git push -u --force origin master
git checkout pelican
