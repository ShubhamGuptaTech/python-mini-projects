a = float(input("enter your 1st operant: "))
b = float(input("enter your 2nd operant: "))
c = input("enter your operator: ")
if (c=="+"):
    print("result: ",a+b)
elif(c=="-"):
    print("result: ",a-b)
elif(c=="*"):
    print("result: ",a*b)
elif(c=="/"):
    if (b==0):
        print("zero devision error")
    else:
        print("result: ",a/b)
else:
    print("invalid operation")