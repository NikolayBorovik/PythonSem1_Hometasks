# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input('Enter your number: '))
sum = 0
while n>0:
    count = n%10
    sum +=count
    n = n//10

print(f"The sum of digits in the number is: {sum}")