print("ET0735 (DevOps for AIoT) - 2 - Introduction to Python")


def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    print(bmi)
    if bmi < 18.5:
        print("You are Under Weight")
    elif bmi >= 18.5 and bmi < 25.0:
        print("You are Normal Weight")
    else:
        print("You are Overweight")

calculate_bmi(weight=57, height=1.73)
