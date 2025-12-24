height = float(input("Enter Height : "))
weight = float(input("Enter Weight : "))
BMI=weight/(height*height)
print("BMI =",BMI)
if 18.5<=BMI<=24:
    print("you is healthy!")
else :
    print("you are not healthy!")