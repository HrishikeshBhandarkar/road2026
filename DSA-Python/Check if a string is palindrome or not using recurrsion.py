#To do this using recurrsion we can use the same logic used to reverse an array using recurrsion
a="malayalam"
def pal(a,l,r):
    if l==r or l>r:
        return "Yes its a palindrome"
    elif a[l]==a[r]:
        return pal(a,l+1,r-1)
    else: return "This is not a palindrome"
print(pal(a,0,8))

