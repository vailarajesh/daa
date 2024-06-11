def arm(n,t):
    if n>0:
        r=n%10
        t=t+(r**3)
        return arm(n//10,t)
    else:
        return t
num=int(input("Enter any number:"))
s=arm(num,0)
if s==num:
    print("Arm strong")
else:
    print("NOT Arm strong")
