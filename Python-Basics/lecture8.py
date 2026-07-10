 # Object oriented programming language
class student:
    def __init__(self,name,roll_no):
        print(self, " This is self")
        self.name=str(name)
        self.roll_no=int(roll_no)
s1=student("Hrishikesh",2598)
print(s1.name)
print(s1, "This is s1")

# __init__ function aka constructor

#Question : To create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def  __init__(self,name,marks_math,marks_physics,marks_chem):#We could also use a list here but i just didn t feel like it
        self.name=name
        self.marks_math=int(marks_math)
        self.marks_physics=int(marks_physics)
        self.marks_chem=int(marks_chem)
    def avg(self):
         total=self.marks_chem+self.marks_math+self.marks_physics
         print("Avarage is %.2f"%(total/3)) #Used the formatinfg thing learned during my 12th 
    @staticmethod 
    def end():
        print('''End
Finished''')
S1=Student("Hrishikesh",93,94,96)
S1.avg()
S1.end()
#STATIC METHODS, methods where self isnt necessary, using a decorator "@staticmethod" implimented on linw 24 and called at line 30

# 2. Create account class with 2 attributes - balance & account number, create method for debit credit and print the balance

class Account:
    def __init__(self,balance,ac_no):
        self.balance=float(balance)
        self.ac_no=int(ac_no)
    def credit(self):
        am=float(input("Enter the amount to be credited to the account = "))
        self.balance+=am
    def debit(self):
        am=float(input("Enter the amount to be debited = "))
        self.balance-=am
    def bal(self):
        print(self.balance)
b1=Account(22229,45)
b1.credit()
b1.debit()
b1.bal()



