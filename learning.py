def calculate_area(width, height):
    area = width * height
    area = area * 1.05
    return area
# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq. ft.") # Room size is 120 sqft