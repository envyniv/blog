#!/bin/sh

shopt -s expand_aliases extglob
#Envy's blog editing utility - track

#YEAR=`date +"%Y"`
#MONTH=`date +"%m"`
#DAY=`date +"%d"`
BLOGINDEX="raw/post-index.json"

if test -f "$1"; then
  FILE=${1//.md}
  FILE=${FILE//"raw/"}

  read -e -p "TAGS > " TAGS
  python3 index-man.py "$BLOGINDEX" "$TAGS" raw/$FILE.md
  if [ $? = 1 ]; then
    echo "Something went wrong with the python script - Operation interrupted"
    exit 1
  fi
  TITLE=$(head -n 1 raw/$FILE.md)
  TITLE=${TITLE#@(# )}
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
fi
