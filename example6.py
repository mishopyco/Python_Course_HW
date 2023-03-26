# Преди доста години имаше услуга - изпращане на луксозна телеграма.
# Поводи най-различни: рожден, имен ден, сватба и т.н. Цената се формираше по следния
# начин А: цена за бланка, B: цена за текст до 20 думи, C: цена за всяка дума, след първите
# 20 думи. Стойностите на A, B, C са реални числа от интервала [0.02..0.89]. Да се състави
# програма, чрез която по въведени брой думи, стойности за A, B, брой думи, C се
# изчислява крайна цена на луксозна телеграма.
# Пример: A=0.2, B=0.5, 45 думи, C=0.05 Изход: 1.95


#Message

print('All prices are real number in the interval between 0.02 and 0.89')
#input
form_price =  float(input ('Enter form price:'))
first_20_words_price = float(input('Enter price for first 20 words of message:'))
word_count=int(input('Enter word count:'))
word_price_after_20 = float(input('Enter price for every word after the 20th:'))

#Calculations
additional_words=word_count-20
total_price_up_to_20_words=form_price+first_20_words_price
total_price_longer_than_20_words=total_price_up_to_20_words+(additional_words*word_price_after_20)

if word_count <= 20:
    print(f'The Price is {total_price_up_to_20_words}')
else:
    print(f'THe price is {total_price_longer_than_20_words}')

