n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
d={}
for i in n:
    d[i]=d.get(i,0)+1
for j in m:
    y=d.get(j,0)
    print(j," repeats ",y,"times in n")

# Character Hashing
s="asdsdhyrtsmdjrdfdfffdserfrkfhsjdmv"
j={}
for i in s:
    j[i]=j.get(i,0)+1
print("Characters present and repeated : ")
for i,k in j.items():
    print(i, "is repeated ",k," times" )