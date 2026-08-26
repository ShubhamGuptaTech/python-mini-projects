a = int(input("English: "))
b = int(input("Math: "))
c = int(input("Science: "))
d = int(input("History: "))
e = int(input("Hindi: "))
subject = ["English", "Math", "Science", "History", "Hindi"]
marks = [a, b, c, d, e]
for i in range(len(marks)):
    if marks[i] == 100:
        print(f"{subject[i]}: O")
    elif marks[i] >= 90:
        print(f"{subject[i]}: A+")
    elif marks[i] >= 80:                            
        print(f"{subject[i]}: A")
    elif marks[i] >= 70:
        print(f"{subject[i]}: B")
    elif marks[i] >= 60:
        print(f"{subject[i]}: C")
    elif marks[i] >= 50:
        print(f"{subject[i]}: D")
    else:
        print(f"{subject[i]}: F")       


    