title: What's it been like maintaining a blog for 3 days
tags: rant,plans,meta,code-dive
syn: My experience maintaining this blog so far

Most of these last few days has been dedicated to getting this blog _just right_.

Down to the tiniest tag inaccuracy or css imperfection (funny, I still have to fix tags)

It's been a draining process so far; But I'm fine with the hurdles, the "growing pains" i've met so far:

> Post titles don't appear in the index page!!!!!!
> WHYYYY?!?!??!?

which, btw, i ended up fixing by changing the python script:

```
for post in posts:
  with open(post, 'r') as file:
    title = file.readline().rstrip().removeprefix("# ")
    file.close()
      
  with open(post, "a") as file:
    ...
```

before, I only had the `with open(post, "a+") as ...`

which, while would work for everything else, it didn't work for reading the first line

TIL: `a+` puts the cursor at the end of the file *for both reading, and writing*

might sound obvious, but i had made an error in comprehension and thought that, while the cursor for _writing_ would be at the bottom,

the one for _reading_ would be at the top.

Funnily enough i did search it up, and got no results, either i'm the only dumb [mf](https://en.wikipedia.org/wiki/Motherfucker) in the python programming landscape, or i just typed my query wrong and [ddg](https://duckduckgo.com/) didn't get what i was looking for.

> My scripts save shit in the wrong places.
> I just formatted my hdd trying to save an HTML file. heh.

... Ok. That didn't happen. not while making this at least.

~~I was trying to automate compilation for [LH](https://envyniv.github.io/Project-Hope) releases, it was over a year ago.~~

Overall, despite the initial, primal rage that awakens within me when my scripts crash, I'm having tons of fun making this; The dopamine hits I get after something miniscule works properly more than make up for all gripes.

~~Hell, now that I have this, I iust might delete [twitter](https://twitter.com/domi_turnell)~~

Also, I'm really enjoying writing blog posts. I could get used to this.

NEXT UPDATE:

```                                                                      
 ???????????????????????????????????????????????????  ??????????????????????????????????????????????????????????????????????????? ???????????????????????? ???????????????   ???????????????????????????????????????
?????????    ?????? ??????    ??????????????????     ?????????   ??????   ?????? ?????? ????????????    ???????????? ????????????    ??? ?????????    ??????
???????????????     ??????   ???  ?????????       ???    ??????      ?????? ?????????      ????????? ??? ?????????   ??? ???????????????    
  ????????????????????? ??????????????????  ??????             ??????      ?????? ??????        ?????? ???  ???????????? ???   ?????????????????????
???     ????????? ??????   ???  ?????????            ??????      ?????? ?????????      ????????? ???   ??????????????? ???     ?????????
??????     ?????? ??????     ???????????????     ??????    ??????      ?????? ????????????    ???????????? ???     ????????? ??????     ??????
????????????????????????????????????????????????????????? ????????????????????????   ??????????????????  ?????????????????? ???????????????????????? ???????????????    ?????? ???????????????????????? 
```
                                                                            
(Y'know, the fancy menus that you can click on that lead you to different parts of a page, right? I'm introducing those next update!!!)


(...)


(maybe, that would require me editing the markdown parser.)

Dunno when i'm gonna start working on that, but for now, I need to take a break from this thing's drunkenly bodged infrastructure.


Also, i've replaced markdown.bash with [_the_ markdown parser](https://daringfireball.net/projects/markdown/)

See you next post,

***envy***.