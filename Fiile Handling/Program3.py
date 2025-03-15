with open("File3.txt", "r") as file:
    cities = file.readlines()
    
    cities.sort()

with open("File3A.txt", "w") as file:
    for city in cities:
        file.write(city)