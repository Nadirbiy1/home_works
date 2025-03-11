
# print("jup" if int(input()) % 2 == 0 else "tak")

print(
    ["Jup" if i % 2 == 0 else "Tak"
     for i in range(1,int(input()) + 1)]
)