#USING LOOPS
n= int(input("Enter a number:"))
# def fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print("Factorial of",n,'is:',fac(n)) 

#USING RECURSION
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
print("Factorial of",n,'is:',fact(n))