with open("File1.txt", "r") as file:
    data = file.read()
    
    words = data.split(" ")

    length = int(input("Enter the word length: "))

    print(f"Words of legnth {length} are: ")
    for word in words:
        if (len(word) == length):
            print(word, end=", ")

    