import urllib2
import pickle

response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

banner = pickle.load(response)
for lst1 in banner:
    line = [c*no for c,no in lst1]
    print "".join(line)
