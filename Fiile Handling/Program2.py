import csv
import math

def dist(coords1, coords2):
    distance = math.sqrt(((int(coords1[0]) - int(coords2[0])) ** 2) +
                          ((int(coords1[1]) - int(coords2[1])) ** 2) +
                          ((int(coords1[2]) - int(coords2[2])) ** 2))
    return distance

with open("File2.csv", mode='r') as file:
    reader = csv.reader(file)

    data_list = []

    for row in reader:
        data_list.append(row)

    min_len = 1000
    min_coords = []

    for i in range(len(data_list)):
        for j in range(i + 1, len(data_list)):
            current_distance = dist(data_list[i], data_list[j])
            if current_distance < min_len:  
                min_len = current_distance
                min_coords = [data_list[i], data_list[j]] 

    print(f"Minimum distance is {min_len} between {min_coords[0]} and {min_coords[1]}")
