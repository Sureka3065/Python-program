def factorial(n)n:
    if n==0:
     return 1
    else:
        return n*factorial(n-1)
    n=int(input("enter the numbber:"))
print("factorial of n is: ",factorial(n))
