#Create a Dictionary of Student Marks

dic = {
    "John": 85,
    "Emma": 92,
    "Sophia": 78,
    "Michael": 88,
    "Olivia": 95,
    "Alice": 85,
    "David": 80,
    "Liam": 90,
    "Noah": 83,
    "Ava": 89,
    "Mia": 91
}
user_input = input("Enter the student's name: ")
if user_input in dic:
    print(user_input + "'s Marks: " + str(dic[user_input]))
else:
    print("Student not found.")