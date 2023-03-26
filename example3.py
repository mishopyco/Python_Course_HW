# рябва да се напълни цистерна с вода. Имате 2 кофи с вместимост 2 и 3 литра
# и ги ползвате едновременно. Да се състави програма, която по въведен обем извежда
# как ще прелеете течността с тези кофи, т.е. по-колко пъти ще се пълни всяка от кофите.
# Входни данни: естествено число от интервала [10..9999].
# Използвайте проверка на логическо условие - оператор if.
# Пример: 107 Изход: 21 пъти 2-те кофи, допълнително кофа от 2 литра

#this code takes volume in liters in the interval [10-9999]
#The input is then used to calculete how many itterations you have to do to fill this volume 
#using 2 and 3 liter increments one after the other untill the volume capacity is reached
#user Input:

# volume = int(input('Enter desired Volume in liters:'))


try:
     volume = int(input('Enter desired Volume in liters:'))

     if  volume<10 or volume>9999:
          raise
except:
     print('your input is out of range')
     exit()

bucket_1 = 2 #volume of first bucket
bucket_2 = 3 #volume of second bucket
total_bucket_volume = bucket_1+bucket_2
times_total_volume_used = volume//total_bucket_volume #How many times both buckets are used together
rest = volume%times_total_volume_used 

#output

if rest==0:
     print(f'Both Buckets are used {times_total_volume_used} times') # if there is no rest

elif rest%bucket_1==0 or rest == 1:
    print(f"""Both Buckets are used {times_total_volume_used} times+ {rest/bucket_1}
      times a 2 litre bucket""")
else:
     print(f"""Both Buckets are used {times_total_volume_used} times+ {rest/bucket_2} 
     times the 3 litre bucket""")

