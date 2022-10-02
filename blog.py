 #!/bin/python3
import json, markdown2, re
from datetime import datetime
from os.path import exists
from os import remove
from os import symlink
#import argparse
from sys import argv

bkIndexFile      = "post-index.html"
indexFile        = "raw/post-index.json"
linkPatternsFile = "raw/patterns.txt"
tagIndexFile     = "raw/tagdesc-index.txt"
y = datetime.now().strftime("%Y")
m = datetime.now().strftime("%m")
d = datetime.now().strftime("%d")
md2set = [ # https://github.com/trentm/python-markdown2/wiki/link-patterns
      "fenced-code-blocks",  # provides triple backtick code block syntax
      "footnotes",           # provides [^<note id>] syntax to add footnotes
      "strike",              # provides ~~<text>~~ syntax for struckthrough text
      "header-ids",          # essentially the same as adding an <a name=slug> tag to every header, can be used as sections
      "spoiler",             # provides stackoverflow blockquote-spoiler syntax  ( >! )
      #"link_patterns"       # swaps given text patterns with links, will be useful for referring to github issues, etc
      ]
pageFormat = """<!DOCTYPE html>
<html>
  <head>
    <title>{t}</title>
    <link rel=icon type='image/svg+xml' href=favicon.svg>
    <link rel=icon type='type=image/png' href=favicon.png>
    <link href=style.css rel=stylesheet type='text/css'>
    <base target="{_}">
  </head>
  <body>
    <embed type='text/html' src=header.html width='100%' height='250px'>
{htmlContent}
    </div>
      <embed type="text/html" src=footer.html width='100%' height='100%'>
    </body>
  </html>
"""
postFormatting = """# {t}

###### Posted on [{yyyy} {mm} {dd}]({i}#{yyyy}-{mm}-{dd})

>#### tags: {tagsHere}

_{s}_

---

{postContent}
"""

def clear_index() -> None:
  """
  Empties the JSON index file.
  """
  with open(indexFile, "w+") as f:
    f.write('{"posts":{ }, "tags": { }, "date":{ }}')
    f.seek(0)
    print(f.read())
    f.close()
  return

def get_link_patterns() -> list:
  """
  Parses the link patterns file and returns them.
  """
  with open(linkPatternsFile) as patternsUnparsed:
    text = patternsUnparsed.read()
    linkPatterns = re.findall(r"^(\S+)\s+(\S+)$", text, flags = re.IGNORECASE | re.MULTILINE)
    linkPatternsParsed = []
    for match in linkPatterns:
      var = re.compile(match[0], re.IGNORECASE), match[1]
      linkPatternsParsed.append(var)
    patternsUnparsed.close()
  return linkPatternsParsed

def print_index() -> None:
  """
  Prints out the index file's contents.
  """
  with open(bkIndexFile, "r") as f:
    print(f.read())
    f.close()
  return

def print_tags() -> None:
  """
  Prints out tags and descriptions.
  """
  with open(bkIndexFile, "r") as f:
    data = json.load(f)
    for tag in data:
      print("\t"+tag+":\t"+fetch_tag_desc(tag))
    f.close()
  return

def fetch_tag_desc(tag: str) -> str:
  """
  Given `tag` exists in the tag desc index, return description.
  """
  with open(tagIndexFile) as index:
    matches = re.findall(r'(.+).*\n*\s*(.+)', index.read(), re.MULTILINE)
    for match in matches:
      if tag == match[0]:
        # print(match[1])
        return match[1]
    index.close()
  return ""


# TODO: ARGPARSE
def main() -> int:
  """
  It starts with one.
  One thing I don't know why,
  It doesn't even matter how hard you try.
  Keep that in mind, I designed this rhyme;
  To explain in due time.
  """
  # argparser

  # parser = argparse.ArgumentParser()
  
  # subparsers = parser.add_subparsers()

  # parser_post = subparsers.add_parser('post')
  # parser_post.add_argument("new")

  # parser_index = subparsers.add_parser('index')
  # parser_index.add_argument("bake", bake())
  # parser_index.add_argument("clear", clear_index())
  # parser_index.add_argument("read", print_index())

  # parser_tags = subparsers.add_parser('tags')
  # #parser_tags.add_argument("add")
  # parser_tags.add_argument("read", print_tags())
  
  # parser.parse_args()
  match argv[1]:
    case "index":
      if argv[2]:
        match argv[2]:
          case "bake":
            bake_index()
          case "clear":
            clear_index()
      else: print_index()
    case "tags":
      print_tags()
    case "add":
      parse_md(argv[2])
  return 0


def index_data() -> dict:
  """
  Returns all data contained in the index file.
  """
  dict = {}
  with open(indexFile, "r+") as json_file:
    dict = json.load(json_file)
    json_file.close()
  return dict

def index_tags(file: str, strtags: str, title: str) -> None:
  """
  Adds `tags` to the JSON index file.
  """
  # strtags.strip() # remove whitespaces
  tags = strtags.split(",")
  with open(indexFile, "r+") as json_file:
    dict = json.load(json_file)

    # post index
    dict["posts"][file] = []
    for tag in tags:
      tag = tag.removeprefix(" ")
      dict["posts"][file].append(tag)

    # index tags in json
    for tag in tags:
      fetch_tag_desc(tag)
      if tag not in dict["tags"]:
        dict["tags"][tag] = {}
      dict["tags"][tag][title] = file

    # index dates
    if y not in dict["date"]:
      dict["date"][y] = {}
    if m not in dict["date"][y]:
      dict["date"][y][m] = {}
    if d not in dict["date"][y][m]:
      dict["date"][y][m][d] = {}
    dict["date"][y][m][d][title] = file

    json_file.seek(0) #resets cursor's position
    json_file.write(json.dumps(dict))
    json_file.truncate() #cuts off old file contents
    json_file.close()
  return

def split_tags(input: str) -> str:
  """
  Returns string of tags with related links.
  """
  tags: str = ""
  for tag in input.split(","):
    tags += "[{e}]({i}#{e}) ".format(e = tag, i = bkIndexFile)
  return tags

def parse_md(filepath: str) -> int: # parse already existing markdown files
  htmlfile = filepath[filepath.rfind("/") + 1 : - len("md")] + "html" #get filepath and strip path, replace extension with html
  with open(filepath) as ogF:
    _temp = ogF.read()
    match = re.search(r'^title:\s*(.+)\n*^tags:\s*(.+)\n*syn:\s*(.+)\n*([\S\s]+)', _temp, re.MULTILINE)
    if not match:
      print("File provided does not match desired structure.")
      return 1
    title = match[1]; tags = match[2]; syn = match[3]; content = match[4] # NOTE: re.Match.group(0) returns ENTIRE match. 1 onwards for groups
    pagecont = postFormatting.format(
      yyyy = y, mm = m , dd = d, i = bkIndexFile, t = title,
      s = syn, tagsHere = split_tags(tags), postContent = content
      )
    ogF.close()
  write_html(htmlfile, pagecont, title)
  index_tags(filepath, tags, title)
  bake_index()
  return 0

def write_html(file: str, content: str, title: str) -> int:
  if exists(file):
    remove(file)
  with open(file, "w+") as target:
    target.write(markdown2.markdown(content, extras = md2set, link_patterns = get_link_patterns()))
    target.seek(0)
    _temp = target.read()

    sections = ""
    extrastyle = ""
    matches = re.findall(r'<h([1-6])\sid="(.+)">(.+)<\/h([1-6])>', _temp, re.MULTILINE)[3:] # all <h#> tags except post header and tags
    if len(matches) > 0:
      extrastyle = ' style="margin-left: 7%; width: 60%; margin-right: 30%"'
      for match in matches:
        sections += '<h%s> <a target="_parent" href=#%s>%s</a> </h%s>\n' % (match[0], match[1], match[2], match[0]) #add link to section, keep level and link in mind
      sections = "<div class=secs><h1>Table of Contents</h1>"+sections+"</div>" # open sections hehehe secs
    target.seek(0)
    target.truncate()
    target.write(pageFormat.format(t = title, _ = "_blank", htmlContent = sections+"<div id=rcorners"+extrastyle+">"+_temp+"</div>"))
    target.close()

    if exists("index.html"):
      remove("index.html")
    symlink(file, "index.html")
  return 0

def bake_index() -> int: #this writes the index page by reading through a json index
  """
  Iterates throughout the JSON index file to write out the html index page.
  """
  # TODO: clean this shit up
  dict = index_data()

  with open(bkIndexFile, "w+") as baked_index:
    baked_index.write("<h2><a name=>By Date</a></h2>")

    for year in dict["date"]:
      baked_index.write("<h3><a name={yearhere}>{yearhere}</a></h3>".format(yearhere=year))

      for month in dict["date"][year]:
        monthString = datetime(int(y), int(m), int(d)).strftime("%B")
        baked_index.write("<h3><a name=%s-%s>%s</a></h3>" % (year, month, monthString))
        baked_index.write("<div class=grid>")

        for day in dict["date"][year][month]:
          dayString = datetime(int(year), int(month), int(day)).strftime("%A")
          baked_index.write("<div><b><a name=%s-%s-%s>%s %s</a></b>" % (year, month, day, dayString, day))
          baked_index.write("<ul>")

          for entry in dict["date"][year][month][day]:
            baked_index.write("<li><a href=%s>%s</a></li>" % (dict["date"][year][month][day][entry].replace(".md", ".html")[dict["date"][year][month][day][entry].rfind("/") + 1 :], entry))

          baked_index.write("</ul>")
          baked_index.write("</div>")
        baked_index.write("</div>")
    baked_index.write("<h2><a name=TAGS>Tags</a></h2>")   

    for tag in dict["tags"]:
      baked_index.write("<h3><a name={name}>{name}</a></h3>\n".format(name=tag))
      baked_index.write("<p id=tagdesc>"+fetch_tag_desc(tag)+"</p>")
      baked_index.write("<div class=grid>")
      for entry in dict["tags"][tag]:
        baked_index.write("<div><a href='%s'>%s</a></div>" % (dict["tags"][tag][entry].replace(".md", ".html")[dict["tags"][tag][entry].rfind("/") + 1 :], entry))
      baked_index.write("</div>")
    baked_index.write("</html>")
    baked_index.seek(0)
    _temp = baked_index.read()
    baked_index.seek(0)
    baked_index.truncate()
    baked_index.write(pageFormat.format(t = "PAGE INDEX", _ = "_parent", htmlContent = _temp))
    baked_index.close()
  return 0

main() #start the whole ordeal