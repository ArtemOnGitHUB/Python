print("Eneter number contains 6 digit :")
number = str(input())
if len(number) != 6:
    print("wrong number") 
elif ((int(number[0])) + (int(number [1])) + (int(number[2])) == 
(int(number[3])) + (int(number[4])) + (int(number[5]))): 
    print("lucky ticket")
else:
    print("unlucky ticket")

# ticket_number = int(input())
# 
# sum_first = 0
# sum_second = 0
#
# while ticket_number:
#   digit = ticket_number % 10
#   if ticket_number > 999:
#       sum_first += digit
#   else:
#       sum_last += digit
#   ticket_number //= 10
#
# print(F"The ticket is lucky: {sum_first == sum_last}")