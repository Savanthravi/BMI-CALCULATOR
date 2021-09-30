name = input("How do you want to enter details si or us: ")
if (name=="si"):
	Height=float(input("enter your Height in m: "))
	Weight=float(input("enter your Weight in kg: "))
	BMI=Weight/(Height*Height)
	print(BMI)
else:
	Height=float(input("enter your Height in inches: "))
	Weight=float(input("enter your Weight in pounds: "))
	BMI=703*Weight/(Height*Height)
	print(BMI)
if(BMI <= 18.4):
	print("you are under weight.")
elif (BMI <= 24.9):
	print("you are healthy.")
elif (BMI <= 29.9):
	print("you are over weight.")
elif (BMI <= 34.9):
	print("you are obesity class1.")
elif (BMI <= 39.9):
	print("you are obesity class2.")
elif (BMI <= 40):
	print("you are obesity class3.")
else:
	print("enter valid details") 