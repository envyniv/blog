 #!/bin/python3

from sys import argv
import json

#mfw this script is here just because dicts in bash are not nice :(

year  = int(argv[1])
month = int(argv[2])
day   = int(argv[3])

post  = argv[5]
name  = argv[6]

index = argv[4]

json_file = open(index, "r+")
dict = json.load(json_file)
  

tags_path = argv[8]
tags_file = open(tags_path, "r")
tags = tags_file.read().split(" ")
tags_file.close()

if argv[7] == "1":
  #create entry
  if year not in dict["by-year"]:
    dict["by-year"][year] = {}
    if month not in dict["by-year"][year]:
      dict["by-year"][year][month] = {}
      if day not in dict["by-year"][year][month]:
        dict["by-year"][year][month][day] = {}
  dict["by-year"][year][month][day][name] = post
  for i in tags:
    i = i.replace("\n","")
    if i not in dict:
      dict["tags"][i]={}
    dict["tags"][i][name] = post
else:
  print("You dumbass, this isn't completed yet")
  #destroy entry

json_file.seek(0)
json_file.write(json.dumps(dict))
json_file.truncate()

#render to html

# code from https://www.w3schools.com/howto/howto_js_dropdown.asp
with open("baked/post-index.html", "w") as baked_index: #will truncate file
  baked_index.write("<!DOCTYPE html>\n<html>")
  id = 0;
  index_js = open("baked/post-index.js", "w")  # will truncate
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