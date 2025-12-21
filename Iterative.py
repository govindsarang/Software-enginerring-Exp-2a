
iterations = int(input("Enter number of iterations: "))

for i in range(1, iterations + 1):
    print(f"\nIteration {i}")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    x = float(input("Enter time (x): "))

    weather = a * x**2 + b * x + c
    print("Weather value:", weather)
