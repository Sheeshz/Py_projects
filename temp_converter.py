
unit = input("Enter unit of temperature(C/F): ")
temp = float(input("Enter temperature: "))

if unit == "C":
    temp = (temp*9/5)+32
    print(f"Temp after convertion is {temp}°F")
elif unit == "F":
    temp = (temp-32)/1.8
    print(f"Temp after convertion is {temp}°C")
else:
    print("Invalid input")