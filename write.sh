#!/bin/sh

shopt -s expand_aliases extglob
alias edit="micro -filetype markdown"
#Envy's blog editing utility
#YEAR=`date +"%Y"`
#MONTH=`date +"%m"`
#DAY=`date +"%d"`

BLOGINDEX="raw/post-index.json"

MARKDOWNSH="./markdown.sh"

TEMP_TAGS="/tmp/tags"

# MAYBE: possibly port index-man.py to this
FILE=`date +"%Y-%j_%k%M-%S"`
edit raw/$FILE.md
if test -f "$FILE.md"; then
  clear
  echo "Write tags, separated by a space. Hyphens in tags will be seen as spaces on the website."
  read -e -p "TAGS > " TAGS
  #IFS=" " read -e -p "TAGS > " -ra TAGS
  #TITLE=$(head -n 1 $FILE.md)
  #TITLE=${TITLE#@(# )}
    # load json into hash, edit as necessary, then dump back into json and parse into html
    #for i in "${TAGS[@]}"; do
    #  $BLOGINDEX
    #done
    #python3 index-man.py $YEAR $MONTH $DAY $BLOGINDEX $FILE.md 1 $TEMP_TAGS
  python3 index-man.py $BLOGINDEX "$TAGS" $FILE.md
  if [ $? = 1 ]; then
    echo "Something went wrong with the python script - Operation interrupted"
    exit 1
  fi
  $MARKDOWNSH $FILE.md > baked/$FILE.html
  echo '<!DOCTYPE html><html><head><link href="baked/style.css" rel="stylesheet" type="text/css"></head><body>' | cat - baked/$FILE.html > temp && mv temp baked/$FILE.html
  echo "</body></html>" >>baked/$FILE.html
  rm latest.html #clear symlink
  ln -s baked/$FILEBAKE.html latest.html
else
  echo "$FILE.md not found, operation cancelled. Did you save?"
fi