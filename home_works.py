# # 1
# res = [i for i in range(1, 21) if i % 2 == 0]
# print(res)
#
# # 2
# res = [i ** 2 for i in range(1, 11)]
# print(res)
#
# # 3
# n = [5, 12, 7, 18, 3, 10, 8]
# res = [i for i in n if i > 7]
# print(res)
#  # 3_2
# #
# print([int(i)for i in input().split(",") if i > 7])
# # 4
# word = ["алма", "банан", "вишня"]
# upper_word = [i.upper() for i in word]
# print(upper_word)
#
# # 5
# number = float(input("Санды киргизиңиз: "))
# res = "оң" if number > 0 else "терс" if number < 0 else "нөл"
# print(res)
#
# print(["on" if int(input()) > 0 else "Ters"])
#
# # 6
# number = int(input("Санды киргизиңиз: "))
# res = "жуп" if number % 2 == 0 else "так"
# print(res)

# 7
numbers = [4, -1, 7, -3, 0, 9, -2]
numbers = [0 if i < 0 else i for i in numbers]
print(numbers)
