R1 = float(input("please give me the first circle's radius \n"))
R2 = float(input("please give me the second circle's radius \n"))
PI = float(input("what is pi? \n"))

S1 = PI*(R1**2)
S2 = PI*(R2**2)

print(f"S1 is {S1} and it's greater than S2 = {S2}") if ( S1 > S2 ) else print("s1 is less than s2")
