#!/bin/sh

shopt -s expand_aliases extglob
#Envy's blog editing utility - track

#YEAR=`date +"%Y"`
#MONTH=`date +"%m"`
#DAY=`date +"%d"`

BLOGINDEX="./raw/post-index.json"

MARKDOWNSH="./markdown.sh"

FILE=$1
read -e -p "TAGS > " TAGS
python3 index-man.py $BLOGINDEX "$TAGS" $FILE
err=$?
if err; then
  echo Something went wrong with the python script - Operation interrupted
  exit 1
$MARKDOWNSH $FILE > baked/$FILE.html
echo '<!DOCTYPE html><html><head><link href="baked/style.css" rel="stylesheet" type="text/css"></head><body>' | cat - baked/$FILE.html > temp && mv temp baked/$FILE.html
echo "</body></html>" >>baked/$FILE.html
rm latest.html #clear symlink
ln -s baked/$FILE.html latest.html
