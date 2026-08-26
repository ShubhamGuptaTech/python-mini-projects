W = float(input("Enter your weight in kg: "))
H = float(input("Enter your height in meters: "))
BMI = W / (H ** 2)
print(f"your BMI is {BMI : .2f}")
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
else:
    print("You are obese.") 