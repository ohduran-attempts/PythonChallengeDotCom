from PIL import Image
import urllib2

response = urllib2.urlopen(
'http://www.pythonchallenge.com/pc/def/oxygen.png')
im = Image.open(response)

pix_val = list(im.getdata())
#629 X 95 pixeles
w,h = im.size

#for i in range(w):
    #print im.getpixel((i,h//2))

#The last part revealed that pixels change every 5 i
def decode(x):
    l = []
    for i in range(w):
        if i % x == 0:
            l.append(im.getpixel((i,h//2))[0])
    return "".join([chr(i) for i in l])

#print decode(5)

# >> smmarrt gguyy, yyouu maadee itt.  thee nnextt lleveel  is  [1105,, 1110,, 1116,, 1101,, 1103,, 1114,, 1105,, 1116,, 1121]]nkca
# print decode(6) >> Nope
# print decode(7)

# >> smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_

# print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))

# >> integrity