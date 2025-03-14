with open("File1.txt", 'r') as file:
    max_len = 0

    text = file.read()
    words = text.split(" ")

    for word in words:
        if (len(word) >= max_len):
            max_len = len(word)

    for i in range(1,max_len+1):
        print(f"Words of length {i}")
        for word in words:
            if (len(word) == i):
                print(word)
        print("\n")

    file.close()

