def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        first = int(str_number[0])
        # Игнорируем ноль, умножая только ненулевые цифры
        return (first if first != 0 else 1) * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если осталась только одна цифра, возвращаем её, игнорируя ноль
        return int(str_number[0]) if str_number[0] != '0' else 1


# Примеры вызовов функции
result = get_multiplied_digits(40203)
print(result)  # 24

result2 = get_multiplied_digits(402030)
print(result2)  # 24
