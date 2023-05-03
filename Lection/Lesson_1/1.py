n = int(input("enter km :"))
m = int(input("enter all km :"))
if n < 0 or m < 0:
    print("idiot")
else:
    print(-(-m//n))
# округление вверх