a=int(input("total marks"))
s1=int(input("first no"))
s2=int(input("second no"))
s3=int(input("third no"))
s4=int(input("fourth no"))
s5=int(input("fifth no"))
c=s1+s2+s3+s4+s5
d=c/a*100
if d>=60 and d<=100:
    print("first divison")
if d>=45 and d<=59:
    print("second divison")
if d>=35 and d<=44:
    print("third division")
if d<35:
    print("fail")