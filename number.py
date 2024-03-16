n = 0; sum = 0 
while True:
    n = int(input("Введите число"))
    if n > 0:
        sum = sum + n
        n = n + 1
    if n == 0:
        break
print("Вы ввели число", n)