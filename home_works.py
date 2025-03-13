def func():
    print("python")
    print("Java")
    print("C++")
    print("#" * 10)

def area_circle():
    radius = float(input("Enter the radius: "))
    s = 3.14 * radius ** 2
    print("Aянт = ", s)

area_circle()

def are_rectangle(width, height):
    if width < 0 or height < 0:
        print("торт бурчтуктун жактары терс болбойт")
    else:
        area = width * height
        print("Аянт = ", area)

are_rectangle(10,11)


def name(names):

    print("Your name's ", names)
name("Arsen")

def name(names):

    print(f"Your name's {names}")
aty = input("Enter your name: ")
name(aty)


