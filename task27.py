print("==================BMI cALCULATOR================")
name=str(input("enter you name:"))
height=float(input("enter height:"))
weight=float(input("enter weight"))
bmi = (weight / height) * height
print("")
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Healthy Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

print("-------------BMI RESULT---------")
print("name:",name)
print("weight:",weight)
print("height:",height)
print("result:",category)