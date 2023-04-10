# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input("Enter n: "))
m = int(input("Enter m: "))
k = int(input("Enter k: "))

if k > m*n:
        print("Don't be too greedy, you're trying to get more than there is(:")
elif k == m*n:
        print("You're trying to have it all, leave something to somebody else:)")
elif k%m == 0 or k%n == 0:
        print("Yes, you can crack it this way!")
else:
        print("No, you cannot crack it this way!")
