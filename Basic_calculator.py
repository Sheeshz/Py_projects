num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

operations = input("Enter an operations(+,-,*,/,%): ")

if operations == "+":
    print(f"the addition is {num1+num2}")
elif operations == "-":
    print(f"the sub is {num1-num2}")
elif operations == "*":
    print(f"the multiply is {num1*num2}")
elif operations == "/":
    if num2 == 0:
        print("Not divisible")
    else:
        print(f"the div is {num1/num2}")
elif operations == "%":
    print(f"the module is {num1%num2}")
else:
    print("FUck off")