#!/bin/sh

shopt -s expand_aliases extglob
alias edit="micro -filetype markdown +1:3"
#Envy's blog editing utility
YEAR=`date +"%Y"`
MONTH=`date +"%m"`
DAY=`date +"%d"`

AUTHOR=`git config --get user.name`
EMAIL=`git config --get user.email`

BLOGINDEX="raw/post-index.json"
# MAYBE: possibly port index-man.py to this
FILE=`date +"%Y-%j_%k%M-%S"`
echo "# \n\n###### $YEAR $MONTH $DAY by [$AUTHOR](mailto:$EMAIL)\n\n---\n\nYour Text Here" >raw/$FILE.md
edit raw/$FILE.md
if test -f "$FILE.md"; then
  clear
  echo "Write tags, separated by a space. Hyphens in tags will be seen as spaces on the website."
  read -e -p "TAGS > " TAGS
  #IFS=" " read -e -p "TAGS > " -ra TAGS
  TITLE=$(head -n 1 $FILE.md)
  TITLE=${TITLE#@(# )}
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
  perl ./Markdown.pl $FILE.md > baked/$FILE.html
  echo "<!DOCTYPE html><html><head><title>$TITLE</title><link rel=icon type='image/svg+xml' href=favicon.svg><link rel=icon 'type=image/png' href=favicon.png><link href=style.css rel=stylesheet type='text/css'></head><body><embed type='text/html' src=header.html width=100% height=250px><div id=rcorners>" | cat - baked/$FILE.html > temp && mv temp baked/$FILE.html
  echo '</div><embed type="text/html" src=footer.html width=100% height=100%></body></html>' >>baked/$FILE.html
  rm latest.html #clear symlink
  ln -s baked/$FILEBAKE.html index.html
else
  echo "$FILE.md not found, operation cancelled. Did you save?"
fi