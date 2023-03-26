# 8. Да се състави програма, която да отгатне колко е студено/топло по
# въведената температура в градус Целзий. Температурните интервали са: t <=-20 ледено
# студено; t <=0 && t>-20 студено; t <=15 && t>0 хладно; t <=25 && t>15 топло; t >25 горещо
# Входни данни: t - цяло число от интервала [-100..100].
# Пример: 12 Изход: хладно
print('T range is between -100 and 100 degrees Celsius')


try:
    temperature= int(input('input T in degrees C')) 
    if -100>temperature or temperature>100:
        raise()
except:
    print ("input out of range") 
    exit()
if temperature <= -20:
    print('T is freezing')
elif 0>= temperature > -20:
    print('T is Cold')
elif 0< temperature <=15:
     print('T is Chilly')
elif 15< temperature <=25:
     print('T is Warm')
else:
     print('T is Hot')