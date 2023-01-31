# Петя, Катя и Сережа делают журавликов. Найдите сколько журваликов
# сделал Катя если извсетно что Петя и Сережа сделали одинковое количество журавликов
# а Катя сделал в два раза больше журавликов, чем Петя
# 6 - 1 4 1
# 24 - 4 16 4
# 60 - 10 40 10

print("Enter number of origami crane :")
crane = int(input())
if crane % 6 != 0:
    print("You entered number that cannot be divided between childrens")
else:
    print(f"Petr made {crane//6}, Serg made {crane//6} and Kate made {(crane//6)*4}")
