#Lecture 7 


#File I/O 
# 1. Adding data to a text file
with open ("practice.txt","r+") as fobj:
    fobj.write("Hi everyone\nWe are learning file I/O\nusing Java\nI like programing")
    fobj.seek(0)
    u=fobj.read()
    ne=u.replace("Java","Python")
    print(ne)
word="learning"
with open ("practice.txt","r") as fobj:
    data=fobj.read()
    if(data.find(word)) != -1:
        print("Found")
    else:
        print("Not found")


def ch_line():
    word="learning"
    data=True
    line_no=1
    with open ("practice.txt","r") as fobj:
        for line in fobj:
            if word in line:
                return line_no
            line_no+=1
print(ch_line())
