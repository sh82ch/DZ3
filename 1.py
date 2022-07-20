#Задача1

import json

keys = ['ingridient_name', 'quantity', 'measure', ]
cook_book_dict = {}

with open('d:/dishes_list.txt', encoding= "utf-8") as text:
    
    lines = []
    for line in text:
        line = line.strip()
        if line:
            lines.append(line)
        continue
    lines = iter(lines)

    # Определяем блюдо и его номер.
    for name in lines:
        cook_book_dict[name] = []
        num = next(lines)
        # Определяем номер линии состава блюда, разбиваем на ингридиенты. 
        for _ in range(int(num)):
            sostav_line = next(lines)
            ingrid = sostav_line.split(' | ')
            z = zip(keys, ingrid)
            sostav_dict = {k: v for (k, v) in z}
            cook_book_dict[name].append(sostav_dict)
            continue
        continue
print('cook_book =', (json.dumps(cook_book_dict, indent=2, ensure_ascii=False)))



# Задача 2
cook_book = {
  'Омлет': [
    {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
    {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}],
  'Утка по-пекински': [
    {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}],
  'Запеченный картофель': [
    {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingridient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}]
}
 
 
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']

    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюдо в расчете на одного человека').capitalize().split(', ')
                
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)
    print()

create_shop_list()


# Задача 3
import os

def create_file_list(folder):
    file_list = os.listdir(folder) 
    join_file_list = []  
    for file in file_list:
        with open(folder + "/" + file) as _temp_file:  
           
            join_file_list.append([file, 0, []])
            for line in _temp_file:
                join_file_list[-1][2].append(line.strip())  
                join_file_list[-1][1] += 1  
   
    return sorted(join_file_list, key=lambda x: x[1], reverse=False)



def create_join_file(folder, filename):
    with open(filename + '.txt', 'w+') as join_file:  
        join_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            join_file.write(f'Название файла: {file[0]}\n') 
            join_file.write(f'Количество строк: {file[1]}\n') 
            for string in file[2]:
                join_file.write(string + '\n')  
            join_file.write('\n')
    return print('Файл создан')


create_join_file('txt', 'join_file')