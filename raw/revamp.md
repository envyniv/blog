title: Major Blog Revamp!
tags: update, meta, test, code-dive
syn: Just revamped the blog, here are some changes.

# Misc minor changes
It's been a while since I last posted, I've taken this time to revamp how this shithole operates:

First off, I've completed the port to python, it ended up being easier than I thought it would be.

Second off, from now on the author's name won't be displayed anymore, mostly because I'm the sole owner of this blog, and because it relied on improper operations, like using `subprocess.run()` to get the username straight from git.

# Posting changes
I've also changed how posting works. Instead of having to write a brand new file from scratch each time, now I just feed the generator script a pre-existing markdown file, making testing easier and avoiding all complications that may arise from third party utilities.

## Tags and where to find them
Being that tags now work "properly", I also need a way to add descriptions to said tags, to display on the index page. Thus I've added *another* file, just for that! It looks like this:

```
my-tag-name-here
This is a very cool tag and this is its description to be displayed in the index page.

my-other-tag
This tag fucking sucks
```

I've gone and fixed all remaining indexing bugs.

# Sections
Sections should now work properly.

# Future changes
- Make html baking for the index page faster (add onto the file, don't rewrite it from scratch)
- - Overall clean up `bake_index()`
- Make the baked index look prettier
- Make 404 page look prettier
  
# Until next time
Overall, as miniscule this project is, it keeps being a learning experience, and an exercise of my patience.

Despite this, I still have to move my code to the `argparse` module.

Until next time, envy.