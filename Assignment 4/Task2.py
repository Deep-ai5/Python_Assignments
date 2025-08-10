txt1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(txt1 + "\n")
print("Data successfully written to output.txt.")

txt2 = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(txt2 + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

