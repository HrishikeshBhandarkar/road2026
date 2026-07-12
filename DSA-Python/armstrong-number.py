# To check if a number is an Armstrong number
a = 153
l = len(str(a))
temp = a
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** l
    temp //= 10
if a == sum :
    print(a, "is an Armstrong number")
else:
    print(a, "yes not an Armstrong number")


   
