def weather(celsius):
    if celsius < 0:
        return "Аба ырайы суук"
    elif 0 < celsius< 20:
        return "Аба ырайы жылуу"
    else:
        return "Аба ырыйы ысык"

print(weather(-10))






