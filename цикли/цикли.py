height = int(input("Введіть висоту: "))
symbol = input("Введіть символ: ")

for i in range(height):
    spaces = height - i - 1
    chars = i + 1
    print(" " * spaces + symbol * chars)



width = int(input("Введіть ширину: "))
height = int(input("Введіть висоту: "))

sym1 = input("Введіть перший символ: ")
sym2 = input("Введіть другий символ: ")

for row in range(height):
    line = ""
    for col in range(width):

        if (row + col) % 2 == 0:
            line += sym1
        else:
            line += sym2
    print(line)






