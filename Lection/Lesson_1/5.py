# a = 5
# d = 6
# c = "gtrrr"
# print(a,d,c)

# a = 5
# d = 6
# c = "gtrrr"
# print(f"{a} - {d} - {c}")

# a = 5
# d = 6
# c = "gtrrr"
# print("{} - {} - {}".format(a,d,c))

# print("Ensert first str")
# a = input()
# print(a)

# print("insert first number")
# a = input()
# b = input("insert second number: ")

# print("insert first number")
# a = input()
# b = input("insert second number: ")

# print(a,' + ', b, ' = ', a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c + '89')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# v = 'fdffd'
# v = int(v)

# print("insert first number")
# a = int(input())
# b = int(input("insert second number: "))

# print(a,' // ', b, ' = ', a // b)

# a = 5.64464
# b = 5.66666
# print(round (a*b, 3))

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)

# username = input('Input name: ')
# if username == 'Mary':
#     print('Its Mary')
# elif username == 'Marina':
#     print('Its Marina')
# elif username == 'Ilnar':
#     print('Ilnar good')
# else:
#     print('Hello,', username)

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + i
# else:
#     print('Its')
#     print('Enough')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag= False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1  
    
# n = int(input())
# a = n // 2
# print(a)

# r = range(100, 0, -20)
# for i in r:
#     print(i)

# a = "qwerty"
# print(a[0])

# a = "qwerty"
# for i in a:
#     print(i)

# line = ""
# for i in range(6):
#     line = ""
#     for j in range(4):
#         line += "+"
#     print(line)

text = "сеШь еще Этих мягких французских булочек"
print(text[0])
print(text[1])
print(text[len(text) -1])
print(text[:2])
print(text[:])
print(text[len(text)-2:])
print(text[2:9])#от 2 идо 9 символа не вклчая 9
print(text[6:-18])#начаная с 6 симвоа с начала и заканчивая 18 симоволом с конца
print(text[0:len(text):6])#с шагом в 6 от начала и до конца
print(text[::6])# c шагом в 6 от начала и до конца
