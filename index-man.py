 #!/bin/python3

from sys import argv
import json
from datetime import datetime
from os.path import exists
from copy import deepcopy

#mfw this script is here just because dicts in bash are not nice :(

# TODO: fix title, line 29
# TODO: title in index
# 

bkIndexFile = "baked/post-index.html"

stylefile   = "style.css"

y  = datetime.now().strftime("%Y") #int(argv[1])
m = datetime.now().strftime("%m") #int(argv[2])
d   = datetime.now().strftime("%d") #int(argv[3])

posts = []
for arg in argv:
  if not (".json" in arg) and not (".py" in arg) and exists(arg):
    posts.append(arg)

with open(bkIndexFile, "w") as baked_index:
  baked_index.write("""
  <!DOCTYPE html>
  <html>
    <head>
      <title>PAGE INDEX</title>
      <link rel=icon type='image/svg+xml' href=favicon.svg>
      <link rel=icon 'type=image/png' href=favicon.png>
      <link href=style.css rel=stylesheet type='text/css'>
    </head>
    <body>
      <embed type='text/html' src=header.html width="100%" height=250px>
      <h1>POST INDEX</h1>

  """)
  for post in posts:
    with open(post, "a+") as content: # get post title
      title = content.readline().rstrip().replace("# ", "")

      index = argv[1]

      json_file = open(index, "r+")
      dict = json.load(json_file)
      tags = argv[2].split(" ")

      if y not in dict["date"]:
        dict["date"][y] = {}
        if m not in dict["date"][y]:
          dict["date"][y][m] = {}
          if d not in dict["date"][y][m]:
            dict["date"][y][m][d] = {}  #YYYYYMCA
      dict["date"][y][m][d][title] = post
      content.write("---\n\n>#### tags : ")
      for tag in tags:
        tag = tag.replace("\n","")
        if tag not in dict:
          dict["tags"][tag] = {}
        dict["tags"][tag][title] = post
        content.write("[{e}](post-index.html#{e}) ".format(e=tag))
      content.write("\n\n")

      content.close()
        
      json_file.seek(0)
      json_file.write(json.dumps(dict))
      json_file.truncate() #truncate manually

      #render to html
      baked_index.write("<h2><a name=>By Date</a></h2>")

      for year in dict["date"]:

        baked_index.write("<h3><a name={yearhere}>{yearhere}</a></h3>".format(yearhere=year))

        for month in dict["date"][year]:

          monthString = datetime(int(y), int(m), int(d)).strftime("%B")
          baked_index.write("<h3><a name=%s-%s>%s</a></h3>" % (year, month, monthString))
          baked_index.write("<div class=grid>")

          for day in dict["date"][year][month]:

            dayString = datetime(int(y), int(m), int(d)).strftime("%A")
            baked_index.write("<div><b><a name=%s-%s-%s>%s</a></b>" % (year, month, day, dayString))
            baked_index.write("<ul>")

            for post in dict["date"][year][month][day]:

              baked_index.write("<li><a href=%s>%s</a></li>" % (dict["date"][year][month][day][post],title))

            baked_index.write("</ul>")
            baked_index.write("</div>")

          baked_index.write("</div>")

      baked_index.write("<h2><a name=TAGS>Tags</a></h2>")   

      for tag in dict["tags"]:
        baked_index.write("<h3><a name={name}>{name}</a></h3>\n".format(name=tag))
        if "💌" in dict["tags"][tag]:
          baked_index.write("<p>%s</p>" % (dict["tags"][tag]["💌"]))
        baked_index.write("<div class=grid>")
        for post in dict["tags"][tag]:
          baked_index.write("<div><a href='%s'>%s</a></div>" % (dict["tags"][tag][post].replace(".md", ".html").replace("raw/", "baked/"), title))
        baked_index.write("</div>")
      baked_index.write("</html>")
      baked_index.close()

      json_file.close()

# WOW, all of that is fucking UNREADABLE; LET'S GOOOOOOo