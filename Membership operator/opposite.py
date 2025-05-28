students = {"Bob", "Marley", "Nikko"}

student = input("Enter the name of a student:")

if student not in students:
    print(f"{student} was not found")   
else:
    print(f"{student} is a student")