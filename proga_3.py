age=float(input('Введіть вік собацюри'))#Блок виведення даних
if age<=2 and age>=0 : age=age*10.5
elif age<0 or age>50 : print('Наврядчи ви ввели вік собаки')
else : age=2*10.5+(age-2)*7
print('Вік собацюри конвертований в людські роки:',age)