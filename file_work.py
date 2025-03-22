# # Записать файл
# with open("file.txt", "w") as file:
#     file.write("Hello world!")
#
# # Дописать в файл
# with open("file.txt", "a") as file:
#     file.write("\nThis is a new line.")
#
# # прочитать файл
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)
#
# # создать файл
# with open("file1.txt", "a") as file:
#     file.write("\nThis is a new line.")
#
#
# # запись и чтение файла
# with open("file.txt", "w+") as file:
#     file.write("Hello, Nadirbiy! \nThis is a new line.")
#     file.seek(0)
#     content = file.read()
#     print(content)


with open('numbers.txt', "w" ) as file:
    for i in range(5):
        number = int(input("Введите число: "))
        file.write(f"{number}\n")

numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(int(line.strip()))
    print(sum(numbers))






