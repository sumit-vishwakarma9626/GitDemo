r = int(input("Enter the number: "))
def fun(n):
    if n<=  1:
        return 1
    else:
        return n * (fun(n-1))
re = fun(r)
print(f"Factorial of {r} is {re}")