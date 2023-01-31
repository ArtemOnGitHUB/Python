# Найдите сумму трехзначного числа

print("Enter three-digit number :")
number = input()
if len(number) !=3:
    print("You enterd a wrong number")
else:
    #if all([i in set(1,2,3,4,5,6,7,8,9) for i in number]):
    print(int(number[0]) + int(number[1]) + int(number[2]))
