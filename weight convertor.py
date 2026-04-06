weight=float(input("enter the weight"))
unit=str("enter the unit of weight (kg/lbs)")

if unit=="kg":
    result=weight*2.205
    print(f"The weight in lbs is {round(result, 2)} {unit}")

elif unit=="lbs":
    result=weight/2.205
    print(f"The weight in kg is {round(result, 2)} {unit}")

else:
    print("Invalid input. Please enter a valid input.")