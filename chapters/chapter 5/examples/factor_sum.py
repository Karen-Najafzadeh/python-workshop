def factorial (N):
    multipul=1
    for i in range (N,0,-1):
            multipul *= i
    return(f"the factorial of {N} is {multipul}")

def sumation (N):
    sum = (N*(N+1)/2)
    return ("sum of 0 to ",N," is: ",int (sum))
