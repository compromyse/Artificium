import math

def hours_to_cover_dish(radius_cm):
    radius_mm = radius_cm * 10
    dish_area_mm2 = math.pi * radius_mm ** 2
    organism_size_mm2 = 1
    hours = 0
    while organism_size_mm2 < dish_area_mm2:
        organism_size_mm2 *= 2
        hours += 1
    
    return hours

radius_cm = int(input().strip())
print(hours_to_cover_dish(radius_cm))
