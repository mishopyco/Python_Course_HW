# Да се състави програма, която ще изчисли сумата на 5, въведени от
# клавиатурата, естествени числа от интервала [10 ..5555].
# Вход: 1,2,3,4,5
# Изход: 15

numbers=input('enter numbers:')
sum_numbers=0
for i in numbers:
    i=int(i)
    sum_numbers+=i
print(sum_numbers)