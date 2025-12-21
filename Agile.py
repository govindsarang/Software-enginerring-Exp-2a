
while True:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    x = float(input("Enter time (x): "))

    weather = a * x**2 + b * x + c
    print("Weather value (Agile Model):", weather)

    choice = input("Run another sprint? (y/n): ")
    if choice.lower() != 'y':
        break
