# This program takes an user input that consist of two 2-digit natural numbers.
#It will give back the last digit of their product and will tell the user if this digit is odd or even.


#input

try:
   a = input('Enter first two digit number:')
   b = input('Enter second two digit number:')
   if (len(a))!=2 or (len(b)) !=2 or int(a)<0 or int(b)<0: #checks if the input is valid 
      raise
except:
   print('Invalid input')
   exit()
#operations

int_a = int(a)
int_b = int(b)
input_product = int_a*int_b
input_product = str(input_product)
product_last_digit= input_product[len(input_product)-1]
product_last_digit = int(product_last_digit)
if (product_last_digit % 2) !=0:
   print(f'the last digit of the product is {product_last_digit} and is odd')
else:
   print(f'the last digit of the product is {product_last_digit} and is even')
