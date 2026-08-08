no=int(input("Enter a number: "))
b=no
s=0
while no!=0:
    c=int(no%10)
    d=c*c*c
    s=s+d
    no=int(no/10)
if s==b:
    print("armstrong number")
else:
    print("not armstrong number")