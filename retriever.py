import urllib2
import os
from bs4 import BeautifulSoup, SoupStrainer
from pprint import pprint

for page in range (1,8):
    print ("Accessing page {}".format(page))
    fo = open("foo_{}.txt".format(page), "wb")
    print ("Log for page {} created".format(page))
    resp = urllib2.urlopen("http://redditlist.com/nsfw?page={}".format(page))
    for link in BeautifulSoup(resp, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            fo.write(link['href'] +'\n')

    fo.close()
    print ("Finished writing")

for info in range(1,8):
    with open('foo_{}.txt'.format(info), 'r') as rfp:
        with open("onelist.txt", 'ab') as wfp:
            for line in rfp:
                if line.startswith("http://reddit.com/r/"):
                    wfp.write(line)

print ("All separate lists concatenated to one list")

print ("Purging duplicate lines...")
lines = open('onelist.txt', 'r').readlines()
lines_set = set(lines) #It can be sorted through the use of sorted()
out  = open('onelist.txt', 'w')
for line in lines_set:
    out.write(line)
out.close()

print ("Duplicate lines purged\nEnd of operation")
os.system("start " + 'onelist.txt')