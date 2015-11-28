import socket
import sys
from urllib.parse import urlparse, urlsplit, urljoin
import os

print (sys.version)

links = open("linklist.txt", "w+")
out = open("iplist.txt", "w+")
lines = open("onelist.txt", "r").readlines()

for line in lines:
    s = "-"
    o = urlparse(line)
    seq = [o.scheme, "://", o.netloc, o.path]
    s.join(seq)
    input = str(s)
    links.write(s)
    # find a way to join the string together without the underlying link


for line in lines:
    try:
        ip = socket.gethostbyname(line) #
        out.write(ip + '\n')
    except socket.gaierror as err:
        print ("cannot resolve hostname: ", line, err)

out.close()
links.close()

# os.system("start " + 'iplist.txt')
os.system("start " + 'linklist.txt')


