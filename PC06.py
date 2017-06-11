#download the file changing the url to .zip instead of .html
def pc06():
    import zipfile

    file = zipfile.ZipFile("channel.zip")

    #read, then follow the breadcrump till the end
    no = 90052
    bool = True
    comments = []
    while bool:
        try:
            text = file.open(str(no)+'.txt').read()
            no = text.split(" ")[-1]
            print int(no)
            comments.append(file.getinfo(str(no) + '.txt').comment)
        except:
            bool = False
            print text


    print "".join(comments)