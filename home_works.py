# 1
res = [i for i in range(1, 21) if i % 2 == 0]
print(res)

# 2
res = [i ** 2 for i in range(1, 11)]
print(res)

# 3
n = [5, 12, 7, 18, 3, 10, 8]
res = [i for i in n if i > 7]
print(res)

# 4
word = ["алма", "банан", "чие"]
capitalized_word = [i.capitalize() for i in word]
print(capitalized_word)

# 5
number = float(input("Санды киргизиңиз: "))
result = "оң" if number > 0 else "терс" if number < 0 else "нөл"
print(result)

# 6
number = int(input("Санды киргизиңиз: "))
res = "жуп" if number % 2 == 0 else "так"
print(res)

# 7
numbers = [4, -1, 7, -3, 0, 9, -2]
updated_numbers = [0 if i < 0 else i for i in numbers]
print(updated_numbers)