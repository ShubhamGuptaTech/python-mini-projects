p = float(input("The amount: ₹"))
r = float(input("Rate of interest (in %): "))
n = float(input("Time (in years): "))
si = (p * r * n) / 100
print(f"You earned ₹{si:.2f} in interest")