n = int(input("Enter Number: "))
prime = True
if n < 2:
    prime = False
else:
    for i in range(2,n):
        if n%i == 0:
            prime = False
            break
if prime:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is not a Prime Number")