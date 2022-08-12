#!/bin/sh

shopt -s expand_aliases extglob
#Envy's blog editing utility - track

#YEAR=`date +"%Y"`
#MONTH=`date +"%m"`
#DAY=`date +"%d"`
BLOGINDEX="raw/post-index.json"
FILE=${1//.md}
FILE=${FILE//"raw/"}

read -e -p "TAGS > " TAGS
python3 index-man.py "$BLOGINDEX" "$TAGS" raw/$FILE.md
if [ $? = 1 ]; then
  echo "Something went wrong with the python script - Operation interrupted"
  exit 1
fi
TITLE=$(head -n 1 $FILE.md)
TITLE=${TITLE#@(# )}
perl ./Markdown.pl $FILE.md > baked/$FILE.html
echo "<!DOCTYPE html><html><head><title>$TITLE</title><link rel=icon type='image/svg+xml' href=favicon.svg><link rel=icon 'type=image/png' href=favicon.png><link href=style.css rel=stylesheet type='text/css'></head><body><embed type='text/html' src=header.html width=100% height=250px><div id=rcorners>" | cat - baked/$FILE.html > temp && mv temp baked/$FILE.html
echo '</div><embed type="text/html" src=footer.html width=100% height=100%></body></html>' >>baked/$FILE.html
rm latest.html #clear symlink
ln -s baked/$FILE.html index.html
