# Да се напише програма, която да създаде следният шаблон:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
number_of_rows = 5
for i in range(0, number_of_rows):
   
    for j in range(0, i + 1):
        # print star
        print("*", end='')
    
    print("\r")

rows=4
for x  in range(0,rows):
   
    for y in range(4,x,-1):
        # print star
        print("*", end='')
    
    print("\r")