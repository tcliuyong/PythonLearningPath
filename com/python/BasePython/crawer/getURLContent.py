# -*- coding:utf-8 -*-
import sys
import os
import HTMLParser
import urllib
import re
import socket
ptitle = re.compile(r"<span class=\"title\">(.*)</span>") #匹配店名字
puname = re.compile(r"span class=\"name vip_level_high\">(.*)</span>")#匹用户名字
pscore = re.compile(r"span class=\"rate-stars\" style=\"width:(.*)%\"")#匹用户名字
socket.setdefaulttimeout(60)
def getCateFromURL(URL):
    dic = {}
    urlText = urllib.urlopen(URL)
    content = urlText.read()
    titles = ptitle.findall(content)
    usernames =  puname.findall(content)
    pscores =  pscore.findall(content)
    dic = dict(map(lambda x,y:[x,y], usernames,pscores))
    if len(titles) > 0:
        return titles[0], dic
    else:
        return None,None