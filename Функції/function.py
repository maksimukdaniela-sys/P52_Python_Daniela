def calculate_discount(price, percent):
    discount = price * (percent / 100)
    final_price = price - discount
    return final_price

result = calculate_discount(200, 15)
print("Ціна після знижки:", result)


def get_grade(points):
    if 90 <= points <= 100:
        return "Відмінно"
    elif 70 <= points <= 89:
        return "Добре"
    elif 50 <= points <= 69:
        return "Задовільно"
    else:
        return "Незадовільно"

print(get_grade(95))
print(get_grade(75))
print(get_grade(60))
print(get_grade(80))
print(get_grade(30))


def rectangle_area(width, height):
    area = width * height
    return area

print(rectangle_area(5, 10))
print(rectangle_area(7, 3))


def analyze_number(num):
    if num > 0:
        return "Додатнє"
    elif num < 0:
        return "Відємне"
    else:
        return "Нуль"

print(analyze_number(3))
print(analyze_number(-72))
print(analyze_number(0))


def average_of_three(a, b, c):
    average = (a + b + c) / 3
    return average

print(average_of_three(3, 7, 10))
print(average_of_three(16, 19, 17))












