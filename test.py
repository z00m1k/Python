#Задание 16 Включить заданное число D в массив A(N) , упорядоченный 
#по возрастанию, с сохранением упорядоченности.
#Для раскраски нужен плагин Colorama 0.4.1 устанавливается следующей командой pip install colorama
import random
from colorama import init  #Расскраска шрифтов
from colorama import Fore, Back#И фонов

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон
spam = int(input("Введите размер массива А: "))     
nums = [random.randint(-500, 500) for i in range(spam)] #Заполнение массива рандомными числами

def cocktail(nums): 					#Коктельная сортировка
    up = range(len(nums) - 1)       
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if nums[i] > nums[i+1]:  
                    nums[i], nums[i+1] =  nums[i+1], nums[i]
                    swapped = True
            if not swapped:
                return nums

cocktail(nums)		#Вызов функции сортировки
D = int(input("Какое число добавить в массив А: "))   
list.append(nums, D) #Добавление на последнее место массива числа D
cocktail(nums)		 #Конечая сортировка массива
print(Back.YELLOW)   #Желтый фон
print("Массив А: " + str(nums))  #Вывод и завершение программы
