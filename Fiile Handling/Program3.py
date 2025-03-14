with open("File3.txt", 'r') as file:
    data = file.read()
    cities = data.split("\n")
    cities.sort()

with open("File3A.txt", 'w') as file:
    for city in cities:
        file.write(city + "\n")