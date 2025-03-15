import csv
import math

def dist(coords1, coords2):
    distance = math.sqrt(((int(coords1[0]) - int(coords2[0])) ** 2) +
                          ((int(coords1[1]) - int(coords2[1])) ** 2) +
                          ((int(coords1[2]) - int(coords2[2])) ** 2))
    return distance
    

with open("File2.csv", mode="r") as file:
    reader = csv.reader(file)

    my_list = []

    for row in reader:
        my_list.append(row)

    print(my_list)

    min_len = 1000

    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            coord1 = my_list[i]
            coord2 = my_list[j]

            dist = dist(coord1, coord2)

            if (dist <= min_len):
                min_len = dist
                min_coords = [coord1, coord2]
    
    print(f"Minimum distance is {min_len} between {min_coords[0]} and {min_coords[1]}")