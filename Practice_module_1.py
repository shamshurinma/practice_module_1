grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]] # Список с оценками учеников в алфавитном порядке
students={'Георгий','Борис','Семён','Константин','Андрей'} # Множество с именами учеников, не в алфавитном порядке
values_1=sum(grades[0])/len(grades[0]) # Ввод переменной со значением средней оценки, путем деления суммы значения индекса 0 списка на поличество символов индекса 0 списка
values_2=sum(grades[1])/len(grades[1]) # Ввод переменной со значением средней оценки, путем деления суммы значения индекса 1 списка на поличество символов индекса 1 списка
values_3=sum(grades[2])/len(grades[2]) # Ввод переменной со значением средней оценки, путем деления суммы значения индекса 2 списка на поличество символов индекса 2 списка
values_4=sum(grades[3])/len(grades[3]) # Ввод переменной со значением средней оценки, путем деления суммы значения индекса 3 списка на поличество символов индекса 4 списка
values_5=sum(grades[4])/len(grades[4]) # Ввод переменной со значением средней оценки, путем деления суммы значения индекса 4 списка на поличество символов индекса 5 списка
students_list_abc=sorted(list(students)) # Ввод переменной с переводом множества с именами учеников в список и сортировка списка учеников в алфавитном порядке
keys_1=students_list_abc[0] # Ввод переменной со значением имени ученика, путем индексирования из списка [0]
keys_2=students_list_abc[1] # Ввод переменной со значением имени ученика, путем индексирования из списка [1]
keys_3=students_list_abc[2] # Ввод переменной со значением имени ученика, путем индексирования из списка [2]
keys_4=students_list_abc[3] # Ввод переменной со значением имени ученика, путем индексирования из списка [3]
keys_5=students_list_abc[4] # Ввод переменной со значением имени ученика, путем индексирования из списка [4]
mid_mark={keys_1:values_1,keys_2:values_2,keys_3:values_3,keys_4:values_4,keys_5:values_5} # Формирование переменной словаря со значениями "Имя ученика:средняя оценка"
print('Средний балл учеников:',mid_mark) # Вывод итоговой переменной со словарем на экран