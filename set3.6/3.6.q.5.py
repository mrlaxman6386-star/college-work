# Write a function calculate_area(radius) that calculates and returns the area of a circle.
def calculate_area (r):
    pi = 3.14159
    area = pi*r**2
    return area  
r=float(input("Enter the radius of the circle: "))
print("The area of the circle is : ",calculate_area(r))