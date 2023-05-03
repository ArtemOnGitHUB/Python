a = int(input("number in first classroom"))
b = int(input("number in second classroom"))
c = int(input("number in third classroom"))
if a or b or c < 0:
    print("idiot")
else:
    print((-(-a//2)) + (-(-b//2)) + (-(-c//2)))
