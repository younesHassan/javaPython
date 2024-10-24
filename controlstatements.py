#create a program that checks if a number is odd or even
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")


#program to check if a person is eligible to vote
name=input("Enter your name: ")
age=int(input("Enter your age: "))

if age>=18:
    print(f"Hey {name}, You are eligible to vote")
else:
    print(f"Hey {name}, You are a minor, you are not eligible to vote")


#create a program that checks the grade of a student
marks=int(input("Enter your marks: "))
if marks <= 100 and marks >= 70:
    print("you got an A")
elif marks <= 69 and marks >= 60:
    print("you got a B")
elif marks <= 59 and marks >= 50:
    print("you got a C")
elif marks <= 49 and marks >= 40:
    print("you got a D")
elif marks <= 39 and marks >=0:
    print("you got a F")
else:
    print("invalid input!")

#CALCULATING BMI
def calculate_bmi(weight_kg, height_m):
  """Calculates the BMI based on weight in kilograms and height in meters.

  Args:
    weight_kg: The weight in kilograms.
    height_m: The height in meters.

  Returns:
    The calculated BMI as a float.
  """

  bmi = weight_kg / (height_m ** 2)
  return bmi

# Get user input
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight_kg, height_m) 


# Print the result
print("Your BMI is:", bmi)