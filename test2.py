#Дан массив размера N. Найти два соседних элемента, сумма которых
#максимальна, и вывести эти элементы в порядке возрастания их
#индексов.

import random
from colorama import init, Fore, Back

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон

spam = int(input("Введите размер массива N: "))     
array = [random.randint(-500, 500) for i in range(spam)] #Заполнение массива рандомными числами
print(Back.YELLOW) 

def search(array):  #Функция для нахождения максимального числа.
	max1 = 0
	for i in range(spam):
		if i >= spam - 1: #Прерывание цикла 
			break
		summa = array[i] + array[i + 1] #Сложение соседних элементов
		if max1 < summa:     #Сравнение прошлой суммы элементов с нынешней
			max1 = summa
	print(Back.CYAN)
	print("Сумма максимальных соседних элементов массива N: " + str(max1))

print("Массив N: " + str(array) + "\n")
search(array) #Вызов функции



