import math

for i in range(1, 4):
    a = float(input(f"Введіть довжину сторони a прямокутника {i}: "))
    b = float(input(f"Введіть довжину сторони b прямокутника {i}: "))
    area = a * b
    print(f"Площа прямокутника {i}: {area}")

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Катет a трикутника 1: "))
b1 = float(input("Катет b трикутника 1: "))
a2 = float(input("Катет a трикутника 2: "))
b2 = float(input("Катет b трикутника 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гіпотенуза трикутника 1: {h1}")
print(f"Гіпотенуза трикутника 2: {h2}")

if h1 > h2:
    print("Гіпотенуза першого трикутника більша.")
elif h1 < h2:
    print("Гіпотенуза другого трикутника більша.")
else:
    print("Гіпотенузи рівні.")

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Центр кола — координата a (x): "))
b = float(input("Центр кола — координата b (y): "))
R = float(input("Радіус кола R: "))

points = {
    "P": (float(input("P1 (x): ")), float(input("P2 (y): "))),
    "F": (float(input("F1 (x): ")), float(input("F2 (y): "))),
    "L": (float(input("L1 (x): ")), float(input("L2 (y): "))),
}

inside_count = 0
for name, (x, y) in points.items():
    if is_inside_circle(x, y, a, b, R):
        print(f"Точка {name} лежить всередині кола.")
        inside_count += 1
    else:
        print(f"Точка {name} не лежить всередині кола.")

print(f"Кількість точок, що лежать всередині кола: {inside_count}")

X = float(input("Сторона X: "))
Y = float(input("Сторона Y: "))
Z = float(input("Сторона Z: "))
T = float(input("Сторона T: "))

right_triangle_area = (X * Y) / 2

diag = math.sqrt(X**2 + Y**2)

s = (Z + T + diag) / 2
heron_area = math.sqrt(s * (s - Z) * (s - T) * (s - diag))

total_area = right_triangle_area + heron_area
print(f"Загальна площа чотирикутника: {total_area}")

n = int(input("Введіть верхню межу n: "))
nums = input("Введіть дільники через пробіл: ").split()
divisors = [int(x) for x in nums]

result = []
for i in range(1, n + 1):
    if all(i % d == 0 for d in divisors):
        result.append(i)

print("Числа, що діляться на всі задані:", result)