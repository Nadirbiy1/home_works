summ = 0
# бул чексиз цикл
while True:
    number = int(input("Введите одно число: "))
    if number == 0:
        # bre
        break
    summ += number
    print(f"общая сумма = {summ}")
