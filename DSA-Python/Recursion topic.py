# Recurrsion using parameters
def pr(c,n):
   if n!=0:
      print(c)
      pr(c,n-1)
pr("Hello World",10)

# Using a tail function
def tl(c, n):
    if n != 1:
        tl(c, n - 1)
    print(c)  


tl("Whats UP", 10)
