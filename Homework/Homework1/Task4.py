# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

#in
#3 2 4
#out
#yes
#in
#3 2 1
#out
#no

print("Enter the number of chocolate slices horizontally")
horizont = int(input())
print("Enter the number of chocolate slices vetically")
vertical = int(input())
print("Enter the number of chocolate slices you want to split")
split = int(input())
if horizont * vertical > split and (split % horizont == 0 or split % vertical == 0):
    print("You can split the chocolate")
else:
    print("You cant split the chocolate")