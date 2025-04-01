import time

parked_cars = {}
RATE_PER_HOUR = 50


def issue_ticket(car_number):
    if car_number in parked_cars:
        return f"Машина {car_number} уже на парковке."

    entry_time = time.time()
    parked_cars[car_number] = entry_time
    return f"Талон выдан для машины {car_number} в {time.ctime(entry_time)}."


def calculate_fee(car_number):
    if car_number not in parked_cars:
        return "Ошибка: машина не найдена на парковке."

    exit_time = time.time()
    entry_time = parked_cars.pop(car_number)
    parked_duration = (exit_time - entry_time) / 3600  # переводим секунды в часы
    fee = round(parked_duration * RATE_PER_HOUR, 2)
    return f"Машина {car_number} находилась {parked_duration:.2f} часов. Сумма к оплате: {fee} сом."


# Пример использования
if __name__ == "__main__":
    while True:
        action = input("Введите '1' для выдачи талона, "
                       "'2' для расчета стоимости, "
                       "'0' для выхода: ")
        if action == '1':
            car_number = input("Введите номер автомобиля: ")
            print(issue_ticket(car_number))
        elif action == '2':
            car_number = input("Введите номер автомобиля: ")
            print(calculate_fee(car_number))
        elif action == '0':
            print("Выход из системы парковки.")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")






