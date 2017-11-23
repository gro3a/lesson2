###Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
###Посчитать и вывести средний балл по всей школе.
###Посчитать и вывести средний балл по каждому классу.
list_of_scores= [
{'school_class':'4a','scores':[3,4,4,5,2]}, 
{'school_class':'4b','scores':[4,2,4,3,5]},
{'school_class':'5v','scores':[5,3,4,2,1,1,1,5]} 
]
for_big_sum= []
sum1=0
for each in list_of_scores:
   sum = 0
   for each2 in each['scores']:
    sum = sum + each2
   print('Средний балл в', each['school_class'], sum/len(each['scores']))
   for_big_sum.append(sum/len(each['scores']))
###   print(for_big_sum)
for each3 in for_big_sum:
    sum1= sum1 + each3
print("Средний балл по школе:", sum1/len(for_big_sum))
