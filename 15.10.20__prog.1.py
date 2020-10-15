list1=[7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
list2 = []
list3 = []
i = 0
while i <= len(list1)-1:
 list2.append((list1[i])*1.3)
 list2[i] = round(list2[i],2)
 list3.append(list2[i] - list1[i])
 list3[i] = round(list3[i],2)
 print('До: ',list1[i],'тис.гривень    ',
 'Після:',list2[i],'тис.гривень    ',
 'Сума індексації склала:',list3[i],'тис.гривень',
 sep = '')
 i += 1