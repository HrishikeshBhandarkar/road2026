# SETS and DICTIONARIES


# 1. Storing word meanings in dictionary
w = {
 "table" : ("a piece of furniture","list of facts and figures"),
  "cat" : "a small animal"
}
print ("Printing a dictionary")
print(w)


# 2. Set problem
l={"python","java","c++","python","javascript","java","python","java","c++","c"}
print("Length of set = ",len(l))

# 3. Program to enter marks 
ma = {}

eng=int(input("Enter ur marks in englisg = "))
mat=int(input("Enter ur marks in maths = "))
cs=int(input("Enter ur marks in cs = "))
ma={"eng" : eng,
"maths":mat,
"cs" : cs}
print(ma)
# Could have also used ma.update({"eng" : eng})
# A way to store 9 and 9.0 in a set
sr={9,"9.0"}
print(sr)
