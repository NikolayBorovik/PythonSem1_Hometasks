# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

ticket = int(input('The number of ticket is: '))

if ticket <100000 or ticket > 999999:
    print("Wrong number.")
else:
     left = ticket//1000
    #  print(left)
     right = ticket%1000
    #  print(right)
sum1 = 0
sum2 = 0
while left>0:
     count1 = left%10
     count2 = right%10
     sum1 +=count1
     sum2 +=count2
     left = left//10
     right = right//10

# print (sum1)
# print(sum2)

if sum1 == sum2:
     print ("The ticket is LUCKY")
else:
     print("The ticket is NOT LUCKY")

