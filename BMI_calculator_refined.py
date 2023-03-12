# This program calculates a persons Body Mass index
#input
weight = int(input('Enter your Weight in kilograms:')) #  weight in kg
height = int(input('Enter your Height in cm:')) #  height in meters
#calculations
bmi = weight/((height/100)**2) #BMI formula

print(f'Your Body Mass Index is {round(bmi)}.')
if  bmi<=18.5:
    print('You are underweight!')
elif 18.5<bmi<24.9:
    print('You have a Normal BMI!')
elif 25<=bmi<29.9:
    print('You are overwieght!')
else: 
    print('You are obese!')