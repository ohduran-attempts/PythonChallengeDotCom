# K --> M
# O --> Q
# E --> G
from string import ascii_lowercase, maketrans

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

def decyphering(s):

    alphabet = ascii_lowercase

    decypher_s = []

    for i in s:
        if i in alphabet:
            ind = alphabet.index(i)
            if ind + 2 >= len(alphabet):
                decypher_s.append(alphabet[ind + 2 - len(alphabet)])
            else:
                decypher_s.append(alphabet[ind + 2])
        else:
            decypher_s.append(i)

    return "".join(decypher_s)

decyphering(s)
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

print decyphering("map")

#ocr