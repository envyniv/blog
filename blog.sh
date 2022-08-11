#!/bin/sh

shopt -s expand_aliases extglob
alias edit="micro -filetype markdown"
#Envy's blog editing utility

YEAR=`date +"%Y"`
MONTH=`date +"%m"`
DAY=`date +"%d"`

BLOGINDEX=post-index.json

MARKDOWNSH=./markdown.sh

TEMP_TAGS="/tmp/tags"

# TODO: possibly port index-man.py to this


if [[ $1 == write ]]; then
  FILE=`date +"%Y-%j_%k%M-%S"`
  edit $FILE.md
  if test -f "$FILE.md"; then
    clear
    echo "Write tags, separated by a space. Hyphens in tags will be seen as spaces on the website."
    read -e -p "TAGS > " TAGS
    #TODAYPATH=${YEAR}/${MONTH}/${DAY}
    #mkdir -p $TODAYPATH
    #ln -s $FILE.md $TODAYPATH/$FILE.md
    #IFR=" " read -e -p -ra "TAGS > " TAGS
    TITLE=$(head -n 1 $FILE.md)
    TITLE=${TITLE#@(# )}
    #for i in "${TAGS[@]}"; do
    #  $BLOGINDEX
    #done
    # I'm not messing with dictionaries in bash, no way
    echo ${TAGS} > $TEMP_TAGS
    python3 index-man.py $YEAR $MONTH $DAY $BLOGINDEX $FILE.md "$TITLE" 1 $TEMP_TAGS
    $MARKDOWNSH $FILE.md > baked/$FILE.html
    echo '<!DOCTYPE html><html><head><link href="style.css" rel="stylesheet" type="text/css"></head>' | cat - baked/$FILE.html > temp && mv temp baked/$FILE.html
    echo "</html>" >>baked/$FILE.html
    rm latest.html #clear symlink
    ln -s baked/$FILE.html latest.html
  fi
  #echo $FILE.md not found, operation cancelled.
fi
if [[ $1 == shred ]]; then
  FILE="$2"
  echo deleting ${FILE}.md
  python3 index-man.py $YEAR $MONTH $DAY $BLOGINDEX $FILE.md "$TITLE" 0 $TEMP_TAGS
  rm ${FILE}.md
fi
