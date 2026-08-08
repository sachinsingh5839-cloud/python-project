a=[]
b=input("press 1 for insert data, 2 for remove data, 3 for find length: ")
if b == "1":
    c=int(input("enter size of tuple: "))
    for i in range(c):
        d=input("enter element: ")
        a.append(d)
    print(a)
elif b == "2":
    e=["admin","18","90.0","bca"]
    for index, value in enumerate(e):
        print(f"{value}=e[{index}]")
    f=input("remove element by location or by value: ")
    if f == "location":
        g=int(input("enter index to remove: "))
        e.pop(g)
        print(e)
    elif f == "value":
            h=input("enter value to remove: ")
            e.remove(h)
            print(e)
elif b == "3":
           i=["admin","18","90.0","bca"]
           print(len(i))
else:
    print("invalid input")