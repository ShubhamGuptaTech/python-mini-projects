def f_to_c():
    f1 = float(input("Enter temperature in  Fahrenheit: "))
    c1 = (f1-32)*(5/9)
    print(f"Temperature in celsius = {c1:.2f}°")
def c_to_f():
    c2 = float(input("Enter temperature in  celsius: "))
    f2 = c2*(9/5)+32
    print(f"Temperature in Fahrenheit = {f2 :.2f}°")

while True:
    print("1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n3. Exit")
    q = int(input("choose option(1-3):"))
    if q==1:
        f_to_c()
    elif q==2:
        c_to_f()
    elif q==3:
        break