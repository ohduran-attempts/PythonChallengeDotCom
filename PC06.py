import urllib2
import string

zipped = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.jpg').read()

unzipped = zip(*zipped)

for line in unzipped:
    print line
