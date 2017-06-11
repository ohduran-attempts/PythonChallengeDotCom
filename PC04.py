#and the next nothing is

import urllib2
def do_numbers(x):
    try:
        while isinstance(x,int):
            response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(x)).read()
            x =  int(str(response).split(" ")[-1])
            print x
    except ValueError:
        print "end"

#Start
#do_numbers(12345)
#the last one is 16044: Divide by two and keep going
do_numbers(16044/2)
#the last one is 66831

#peak.html