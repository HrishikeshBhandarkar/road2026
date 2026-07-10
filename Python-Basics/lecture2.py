# Program to input users first name and display its length
n = input('Enter your name = ')
print("The length of your name is = ", len(n))

#Program to find the occurance of $ in a string
w = "He spends a lot of dollars $$$$"
print(w)
print("Total $ in the sentence is = ",w.count("$"))

#Program to check if the entered number is even or odd
print("Check if entered number is odd or even")
a = int(input("Enter ur number = "))
if a%2==0:
 print(a," is even")
else:
 print(a,"is odd")


# Program to find greatest of 3 numbers entered by user
print("Enter 3 numbers and the largest number will be printed ")
a1=int(input("Enter your number = "))
a2=int(input("Enter you number = "))
a3=int(input('Enter your number = '))
if a1>a2 and a1>a3:
 g=a1
elif a2>a3:
 g= a2
else:
 g=a3
print("The greatest amoung three is = ",g)


#Program if the entered number is the multiole of 7
print("To check if the number is divisible by 7")
qq=int(input("Enter a number = "))
if qq%7==0:
 print(qq," is divisible by 7")
else:
 print(qq," is not divisible by 7")

