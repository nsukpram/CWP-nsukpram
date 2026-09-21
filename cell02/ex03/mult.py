num1 = input("Enter the first number:\n").strip()
num2 = input("Enter the second number:\n").strip()
x = int(num1)*int(num2)
print(f"{num1} x {num2} = {x}")
if x > 0 :
    print("The result is positive.")
elif x < 0 :
    print("The result is negative.")
else :
    print("The result is positive and negative.")