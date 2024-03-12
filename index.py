import math

def count_points_in_circle(radius):
    count = 0
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x**2 + y**2 <= radius**2:
                count += 1
    return count

radius = int(input('ввидите число'))
result = count_points_in_circle(radius)
print(f"Всего  точек в радиусе {radius}")