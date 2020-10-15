print('Після кожного окремого елемента натисніть "Enter"'
'\nЩоб завершити введеня даних, після останнього елемента ДВІЧІ натисніть "Enter"')
list1 = []
x = str(input('Введіть перший елемент :'))
list1.append(x)
while True:
    x = str(input('Введіть наступний елемент :'))
    if x == '':
        break
    else:
        list1.append(x)
if len(list1)!=0:
    print(list1[0], end = '')
i = 1
while i <= len(list1)-2:
    print(',',list1[i], end = '')
    i += 1
if len(list1) >= 2 :print(' and',list1[-1])