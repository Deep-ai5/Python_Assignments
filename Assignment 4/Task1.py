try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        lines = file.readlines()
        for i in range(len(lines)):
            print("Line " + str(i+1) + ": " + lines[i].strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

