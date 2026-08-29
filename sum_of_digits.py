num = input("Enter Number: ")
total = 0
for digit in num:
    total += int(digit)
print(f"Sum of digits of {num} is {total}")