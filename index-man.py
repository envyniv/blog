 #!/bin/python3

from sys import argv
import json
from datetime import datetime
from os.path import exists
from copy import deepcopy

#mfw this script is here just because dicts in bash are not nice :(

# TODO: fix title

bkIndexFile = "baked/post-index.html"
bkIndexJS   = "baked/post-index.js"

year  = datetime.now().strftime("%Y") #int(argv[1])
month = datetime.now().strftime("%m") #int(argv[2])
day   = datetime.now().strftime("%d") #int(argv[3])

posts = []
for arg in argv:
  if not ".json" in arg &&  not ".py" in arg && exists(arg):
    posts.append(arg)
for post in posts:
  with open(post) as content: # get post title
    title = content.read()
    title.split("\n")
    title = title[0].replace("# ", "")
    content.close()

    index = argv[1]

    json_file = open(index, "r+")
    dict = json.load(json_file)
    tags = argv[2].split(" ")

    if year not in dict["by-year"]:
      dict["by-year"][year] = {}
      if month not in dict["by-year"][year]:
        dict["by-year"][year][month] = {}
        if day not in dict["by-year"][year][month]:
          dict["by-year"][year][month][day] = {}
    dict["by-year"][year][month][day][title] = post
    for i in tags:
      i = i.replace("\n","")
      if i not in dict:
        dict["tags"][i] = {}
      dict["tags"][i][title] = post
      
    json_file.seek(0)
    json_file.write(json.dumps(dict))
    json_file.truncate() #truncate manually

    #render to html

    # code from https://www.w3schools.com/howto/howto_js_dropdown.asp
    with open(bkIndexFile, "w") as baked_index: #will truncate file
      baked_index.write("<!DOCTYPE html>\n<html>")
      id = 0;
      index_js = open(bkIndexJS, "w")  # will truncate
      for tag in dict["tags"]:
        baked_index.write("<head><link href='style.css' rel='stylesheet' type='text/css'><script src='post-index.js'></script></head>")
        baked_index.write("<div class=dropdown>\n\t<button onclick='%sFunction()' class=dropbtn>%s</button>\n\t<div id=%sDropdown class=dropdown-content>" % (tag, tag, tag))
        index_js.write("\nfunction %sFunction() { document.getElementById('%sDropdown').classList.toggle('show'); }" % (tag, tag))
        for post in dict["tags"][tag]:
          baked_index.write("<a href='%s'>%s</a>" % (dict["tags"][tag][post].replace(".md", ".html"), post))
      index_js.write("""
    window.onclick = function(event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }""")
      baked_index.write("\t</div>\n</div>\n</html>")
      baked_index.close()
      index_js.close()

    json_file.close()