#this code uses the lenght and widht of a rectangle to calculate
# the perimeter and surface area of a rectangle and gives message if the figure is a square.
#All values are to be given in milimeters and have to be natural whole numbers in the interval [5...100]


print('Please define your figure by giving lenght and widht. Both must be whole numbers between 5 an 100')
try:   
    widht = int(input('Enter widht in mm: '))
    lenght =  int(input('Enter lenght in mm: '))
   
    if widht>100 or widht<5 or lenght>100 or lenght<5:
       raise
except:
    print('Invalid input')
    exit()
    

perimeter = 2*(widht+lenght)
surface_area = widht*lenght

if lenght==widht:
    print(f'Widht and lenght are equal. This means your figure is a Square')
print(f'The perimeter is {perimeter}mm and the surface area is {surface_area} square milimiters')