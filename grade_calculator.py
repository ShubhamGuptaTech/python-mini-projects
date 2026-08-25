a = float(input("Science: "))
b = float(input("Mathematics: "))
c = float(input("English: "))
d = float(input("Social Science: "))
e = float(input("Hindi: "))
marks = [a,b,c,d,e]
for i in marks:
    if(i==100):
        print("O")
    elif (i>= 90):
        print("A+")
    elif(i >= 80):
        print("A")
    elif(i >= 70):
        print("B")
    elif(i >= 60):
        print("C")
    elif(i >= 50):
        print("D")
    else:
        print("FAIL")

        