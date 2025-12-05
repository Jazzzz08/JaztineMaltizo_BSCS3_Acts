import math

# Task 2.1: Coordinate System with Tuples

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

# Input points
p1 = tuple(map(float, input("Enter Point 1 (x y): ").split()))
p2 = tuple(map(float, input("Enter Point 2 (x y): ").split()))
p3 = tuple(map(float, input("Enter Point 3 (x y): ").split()))

points = (p1, p2, p3)

print(f"\nAll Points: {points}")
print(f"Distance between P1 and P2: {distance(p1, p2):.2f}")
print(f"Midpoint between P1 and P2: {midpoint(p1, p2)}")

# Demonstrate immutability
try:
    points[0] = (0, 0)
except TypeError:
    print("Error: Tuples are immutable!")
