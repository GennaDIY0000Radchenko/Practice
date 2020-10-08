try:
    mark=int(input('Plese , enter mark:'))#Блок введення даних
    if mark>100:print('You enter mark , which heigher then 100')
    elif mark<=100 and mark>=95 :print('Excellent')#Блок виведення даних
    elif mark<=94 and mark>=85 : print('Very good')#Блок виведення даних
    elif mark<=84 and mark>=75 : print('Good')#Блок виведення даних
    elif mark<=74 and mark>=65 : print('Satisfactory')#Блок виведення даних
    elif mark<=64 and mark>=60 : print('Marginal')#Блок виведення даних
    elif mark<=59 and mark>=0 :  print('Unsatisfactory')#Блок виведення даних
    else : print("You enter negative mark")
except ValueError:print("Ви ввели не число")