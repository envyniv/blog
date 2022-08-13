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
echo "# 

###### $YEAR $MONTH $DAY by [$AUTHOR](mailto:$EMAIL)

_Post Synopsis Here_

---

Your Text Here" >raw/$FILE.md

edit raw/$FILE.md
if test -f "$FILE.md"; then
  echo "Write tags, separated by a space. Hyphens in tags will be seen as spaces on the website."
  read -e -p "TAGS > " TAGS
  #IFS=" " read -e -p "TAGS > " -ra TAGS
  TITLE=$(head -n 1 raw/$FILE.md)
  TITLE=${TITLE#@(# )}
  python3 index-man.py $BLOGINDEX "$TAGS" $FILE.md
  if [ $? = 1 ]; then
    echo "Something went wrong with the python script - Operation interrupted"
    exit 1
  fi
  perl ./Markdown.pl raw/$FILE.md > $FILE.html
 echo "
<!DOCTYPE html>
<html>
  <head>
    <title>$TITLE</title>
    <link rel=icon type='image/svg+xml' href=favicon.svg>
    <link rel=icon 'type=image/png' href=favicon.png>
    <link href=style.css rel=stylesheet type='text/css'>
  </head>
  <body>
    <embed type='text/html' src=header.html width=100% height=250px>
    <div id=rcorners>" | cat - $FILE.html > temp && mv temp $FILE.html
echo '    </div>
    <embed type="text/html" src=footer.html width=100% height=100%>
  </body>
</html>' >>$FILE.html
  rm index.html #clear symlink
  ln -s $FILE.html index.html
else
  echo "$FILE.md not found, operation cancelled. Did you save?"
fi