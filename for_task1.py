###Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
###Посчитать и вывести средний балл по всей школе.
###Посчитать и вывести средний балл по каждому классу.
list_of_scores= [
{'school_class':'4a','scores':[3,4,4,5,2]}, 
{'school_class':'4b','scores':[4,2,4,3,5]},
{'school_class':'5v','scores':[5,3,4,2,1,1,1,5]} 
]
for_big_sum= []
sred_po_shkole=0
for each in list_of_scores:
   summa_po_klassu= 0
   for ocenka in each['scores']:
    summa_po_klassu += ocenka
    ocenka_v_klasse=int(ocenka)
    for_big_sum.append(ocenka_v_klasse)
   print('Средний балл в', each['school_class'], summa_po_klassu/len(each['scores']))
sred_po_shkole=sum(for_big_sum)/len(for_big_sum)
print('Средний балл по школе: ' , sred_po_shkole)
