title: TIL: How to bodge a blog from scratch
tags: meta,test
syn: Some of my shenanigans while trying to have everything work the way it should.

Hello, and welcome to the first serious post on this blog of mine! I'm gonna cut to the chase and talk a bit about the behind the scenes.

I've been wanting to make a blog for some time, mainly to publish notes and give out updates on my projects.

But everytime i looked up stuff like `how 2 setuPP jekyll with my poopoo html` i was put off by the tutorials. Heck, I tried following one and it just didn't work.

Another thing i dislike about Stuff like Hugo and Jekyll is that, to run them, a standalone webserver is needed.

And, while, yes I do have the technical skills to set one up (It really isn't hard, at all.) I just felt that a webserver for my shitty blog would be overkill.

(Also I'd need to set up stuff on GitHub, which annoys me.)

So, I thought of parsing Markdown files into html and then showing those.

"It would only require a script and some time" - I thought to myself.

And I was... _somewhat_ right, actually.

Why somewhat? because i can't `bash` were it for the life of me.

It's just... so unnatural to me. The problem mainly arose when i got to parsing a JSON into a dictionary, and found out that bash doesn't have those.

So, being a python shill, that's what i went with;

And that's why the write script calls `python3 index-man.py`, because I felt that learning [_Associative Arrays_](https://linuxhint.com/associative_array_bash) were too much of an issue for something supposed to be a quick bodge.

I also initially wanted to parse markdown myself, but got lazy and opted for [markdown.bash](https://github.com/chadbraunduin/markdown.bash/)

I plan on eventually<sup>TM</sup> porting `index-man` into bash, but for now...

I'll just focus on fixing my website. And maybe keep working on [Last Hope](https://envyniv.github.io/Project-Hope/).

~~Hopefully those two html tags i used for a joke don't break the whole thing~~