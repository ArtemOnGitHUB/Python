a = int(input("number of year: "))
if (a % 4 == 0 and a % 100) or a % 400 == 0:
    print("yes")
else:
    print("no")