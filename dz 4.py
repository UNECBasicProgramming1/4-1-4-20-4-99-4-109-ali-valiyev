# 4.1
a = float(input())
b = float(input())
if a > b:
    print(a, b)
else:
    print(b, a)

# 4.2
import math
x = float(input())
if x > 0:
    y = math.sin(x)**2
else:
    y = 1 - 2 * math.sin(x)**2
print(y)

# 4.3
x = float(input())
if x > 0:
    y = math.sin(x)**2
else:
    y = 1 + 2 * math.sin(x)**2
print(y)

# 4.4
x = float(input())
y = float(input())
if x < 4:
    print("I")
else:
    print("II")

# 4.5
x = float(input())
y = float(input())
if y > 3:
    print("I")
else:
    print("II")

# 4.6a
x = float(input())
if x <= 2:
    y = x
else:
    y = 2
print(y)

# 4.6b
x = float(input())
if x <= 3:
    y = -x
else:
    y = -3
print(y)

# 4.7
import math
x = float(input())
if math.sin(x) < 0:
    k = x**2
else:
    k = abs(x)
if k < x:
    f = k * x
else:
    f = k + x
print(f)

# 4.8
import math
x = float(input())
if math.sin(x) >= 0:
    k = x**2
else:
    k = abs(x)
if x < k:
    f = abs(x)
else:
    f = k * x
print(f)

# 4.9
a = float(input())
b = float(input())
max_val = a if a > b else b
min_val = a if a < b else b
print("max =", max_val)
print("min =", min_val)

# 4.10
km = float(input())
ft = float(input())
m1 = km * 1000
m2 = ft * 0.3048
if m1 < m2:
    print("Меньше расстояние в километрах")
else:
    print("Меньше расстояние в футах")

# 4.11
v1 = float(input())  # км/ч
v2 = float(input())  # м/с
v1_m_s = v1 / 3.6
if v1_m_s > v2:
    print("Больше скорость в км/ч")
else:
    print("Больше скорость в м/с")

# 4.12
import math
r = float(input())
a = float(input())
s_circle = math.pi * r**2
s_square = a**2
if s_circle > s_square:
    print("Больше площадь круга")
else:
    print("Больше площадь квадрата")

# 4.13
v1 = float(input())
m1 = float(input())
v2 = float(input())
m2 = float(input())
p1 = m1 / v1
p2 = m2 / v2
if p1 > p2:
    print("Первое тело плотнее")
else:
    print("Второе тело плотнее")

# 4.14
r1 = float(input())
u1 = float(input())
r2 = float(input())
u2 = float(input())
i1 = u1 / r1
i2 = u2 / r2
if i1 < i2:
    print("Меньший ток в первом участке")
else:
    print("Меньший ток во втором участке")

# 4.15
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if d > 0:
    print("Два корня")
elif d == 0:
    print("Один корень")
else:
    print("Нет действительных корней")

# 4.16
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if d < 0:
    print("Нет действительных корней")
else:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print("x1 =", x1, "x2 =", x2)

# 4.17
birth_year = int(input())
birth_month = int(input())
now_year = int(input())
now_month = int(input())
age = now_year - birth_year
if now_month < birth_month:
    age -= 1
print(age)

# 4.18
import math
r = float(input())
a = float(input())
if 2 * r <= a:
    print("Круг поместится в квадрат")
else:
    print("Круг не поместится в квадрат")
if a * math.sqrt(2) <= 2 * r:
    print("Квадрат поместится в круг")
else:
    print("Квадрат не поместится в круг")

# 4.19
import math
r = float(input())
a = float(input())
h_triangle = math.sqrt(3) / 2 * a
if 2 * r <= h_triangle:
    print("Круг поместится в треугольник")
else:
    print("Круг не поместится в треугольник")
if h_triangle <= 2 * r:
    print("Треугольник поместится в круг")
else:
    print("Треугольник не поместится в круг")

# 4.20
x1_left = float(input())
y1_left = float(input())
x2_left = float(input())
y2_left = float(input())
x1_right = float(input())
y1_right = float(input())
x2_right = float(input())
y2_right = float(input())
x_min = min(x1_left, x1_right)
y_min = min(y1_left, y1_right)
x_max = max(x2_left, x2_right)
y_max = max(y2_left, y2_right)
print(x_min, y_min, x_max, y_max)

# 4.99
a = float(input())
b = float(input())
max_val = a
if a < b:
    max_val = b
print(max_val)
max_val = a
max_val = b if b > a else max_val
print(max_val)

# 4.100
a = float(input())
b = float(input())
max_val = a
min_val = a
if a < b:
    max_val = b
if a > b:
    min_val = b
print(max_val, min_val)
max_val = a if a > b else b
min_val = b if a > b else a
print(max_val, min_val)

# 4.101
a = float(input())
b = float(input())
c = float(input())
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print(max_val)
min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
print(min_val)

# 4.102
a = float(input())
b = float(input())
c = float(input())
d = float(input())
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if d > max_val:
    max_val = d
print(max_val)
min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
if d < min_val:
    min_val = d
print(min_val)

# 4.103
x = float(input())
if x < 0:
    x = -x
print(x)

# 4.104
import math
a = float(input())
b = float(input())
abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b
print((abs_a + abs_b)/2)
print(math.sqrt(abs_a*abs_b))

# 4.105
a = float(input())
b = float(input())
abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b
if abs_a > abs_b:
    a = a / 2
print(a)

# 4.106
import math
a = float(input())
b = float(input())
if math.sqrt(b) < a:
    b = b * 5
print(b)

# 4.107
x = int(input())
y = int(input())
z = int(input())
for num in (x, y, z):
    if num % 2 == 0:
        print(num)

# 4.108
a = float(input())
b = float(input())
c = float(input())
if a >= 0:
    a = a**2
if b >= 0:
    b = b**2
if c >= 0:
    c = c**2
print(a, b, c)

# 4.109
a = float(input())
b = float(input())
c = float(input())
for num in (a, b, c):
    if 1.6 <= num <= 3.8:
        print(num)
