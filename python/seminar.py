# # В некоторой школе решили набрать три 
# # новых математических класса и
# # оборудовать кабинеты для них новыми партами.
# # За каждой партой может сидеть два учащихся.
# # Известно количество учащихся в каждом
# # из трех классов. Выведите наименьшее число парт, 
# # которое нужно приобрести для них.
# # input 
# # 20
# # 21
# # 22
# # uotput 
# # 32
# import math
# firstclass = 20
# secondclass = 21
# thirdclass = 22
# bench_sum = (math.ceil(firstclass/2)
#      + math.ceil(secondclass/2)
#      + math.ceil(thirdclass/2))
# print(bench_sum)

# # days = total//per_day + (total%per_day != 0)


# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, 
#              а иногда – с «хвоста»; это зависит от того,
#                в какую сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке. 
# Напишите программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать невозможно.

# **Input:**

# 3

# 4

# **Output:*
 
# Дано натуральное число. 
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100,
# а также если он кратен 400.

# **Input:**

# 2016

# **Output:**

# year = int (input('введите год:'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('yes')
# else:
#     print('no')

# n = int(input('Введите число: '))
# i = 1
# f = 1
# while i<=n:
#     f = f*i
#     f+=1
    

# number_a = int(input('Введите число: '))

# fibo1 = 0
# fibo2 = 1
# counter = 0
# while fibo1 + fibo2 <= number_a:
#     fibo1 = fibo1 + fibo2
#     fibo2 = fibo2 + 1
#     counter += 1
# if fibo1 == number_a:
#     print(counter)
# else:
#     print(-1)

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, 
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.


# from random import randint


# n = int(input('Введите количество арбузов'))




# from random import randint

# count_wm = int(input('Введите количество арбузов: '))

# max_wm = float('-inf')
# min_wm = float('inf')
# print(f'Перед вами {count_wm} арбузов:')
# for _ in range(count_wm):
#     current_wm = randint(1000, 30000)
#     print(current_wm, end=' ')
#     if max_wm < current_wm:
#         max_wm = current_wm
#     if min_wm > current_wm:
#         min_wm = current_wm
# print(f'\nСамый тяжелый арбуз - {max_wm} гр\nСамый легкий арбуз - {min_wm} гр')


# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, 
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.


# from random import randint

# temp = 0
# counter = 0
# max_days = 0
# days = int(input('Введите количество дней: '))

# for _ in range(days):
#     temp = randint(-10, 10)
#     print(temp, end=' ')
#     if temp > 0:
#         counter = counter + 1 
#         if max_days < counter:
#             max_days = counter
#     else: 
#         counter = 0
# print()    
    
# print(max_days)

    
# print('Это не трехзначное число! ')
# if n > 99 and n < 1000:
#     a = n % 10
#     b = n // 10
#     c = b % 10
#     j = b // 10
#     res = j + c + a
# print(res)


# n = int(input('Введите трехзначное число: '))

# if n > 99 and n < 1000:

#     a = n % 10
#     b = (n % 100) // 10
#     c = b // 10
#     res = a + b + c
#     print(res)

# n = int(input('Введите трехзначное число: '))
# n1 = n // 100
# n2 = (n % 100) // 10
# n3 = n % 10
# res = n1 + n2 + n3
# print (res)

# ticket = int(input('введите: '))

# first = ticket[:3]
# second = ticket[3:]

# first = int(first[0]) + int(first[1]) + int(first[2])
# second = int(second[0]) + int(second[1]) + int(second[2])
# print('Не'*(first != second) + 'счастливый')


# number = input("введите: ")

# count_dict = {}

# for i in number:
#     count_dict[i] = count_dict.get(i, 0) + 1
#     print(f'{i}' + (f'_{count_dict[i] - 1}' if count_dict[i] > 1 else ''), end=' ')


# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов
# # идущих подряд, 
# # слова разделены одним или большим числом пробелов или 
# # символами конца строки.Определите, сколько различных 
# # слов содержится в этом тексте.


# n = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells"""

# # n = input("введите строку: ")
# # n = n.lower()

# # n = n.replace('.', ' ')
# # print(n)

# # n = list(n.split())
# # n_set = set(n)


# # print(n_set)
# # print(len(n_set))



# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#      max_number = n
# print(max_number)

# n = int(input("введите: "))

# max_number = n
# while n > 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

