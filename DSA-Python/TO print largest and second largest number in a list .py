#TO print largest and second largest number in a list 
a =[35, 12, 1, 10, 34, 1]
max = float('-inf')
s = float('-inf')
for i in a:
    if i > max:
        max = i
for i in a:
    if i < max and i > s:
        s=i
if max == s:
    s = -1
print("Second largest element is = ",s)
print("Largest element is = ",max)

