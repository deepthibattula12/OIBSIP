def bmi_function(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

if __name__ == "__main__":
    w1 = float(input("Enter your weight in kilograms: "))

    # Get height in meters from the user
    h1 = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = bmi_function(w1, h1)

    # Print the calculated BMI
    print("Your BMI is:", bmi)

    # Interpret BMI
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("Your weight is normal.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")