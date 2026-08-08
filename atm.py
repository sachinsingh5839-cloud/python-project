a = int(input("Enter PIN: "))
if a == 1234:
    print("Correct PIN")
    b = input("Press 1 for balance, 2 for deposit, 3 for withdrawal: ")
    if b == "1":
        print(1000)
    elif b == "2":
        e = int(input("Enter amount: "))
        h = 500 + e
        print(h)
    elif b == "3":
        f = int(input("Enter amount: "))
        if f > 500:
            print("Insufficient balance")
        else:
            g = 500 - f
            print(g)
else:
    print("Incorrect PIN")