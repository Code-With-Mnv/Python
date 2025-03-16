import csv
import math

def calculate_distance(coords1, coords2):
    return math.sqrt(((coords1[0] - coords2[0]) ** 2) +
                     ((coords1[1] - coords2[1]) ** 2) +
                     ((coords1[2] - coords2[2]) ** 2))

with open("File2.csv", mode="r") as file:
    reader = csv.reader(file)

    points = []

    for row in reader:
        points.append([int(row[0]), int(row[1]), int(row[2])])

if len(points) < 2:
    print("Not enough points to calculate distance.")
else:
    min_distance = float('inf')
    closest_points = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_points = (points[i], points[j])

    print(f"Minimum distance is {min_distance} between {closest_points[0]} and {closest_points[1]}")
