#b Lecture based on lists and tuples
# 1. TO ask user their 3 favourite movies and store them in a list
print("To ask users their 3 most favourite movies = ")
l=[]
i=1
for i in range(3):
 l.append(input("Enter your ",i," favourite movie = "))
 i+=1
print(l)


# To check if a list contains palindrome of elements
print("To check if list contains palindrome of elements ")
lo=[1,2,1]
print(lo)
i=lo
if i.reverse==lo:
 print("Yes its a palindrome")
else:
 print("NO it isnt a palindrome ")


#  To count number of students withg grade a in a tuple
gr=("C","D","A","A","B","B","A")
print("To count number of students with grade 'A'")
print(gr)
print(gr.count("A")

print("Now storing them and sorting them,however we convert it first to a list")
o=list(gr)
print(o)
print(o.sort())

