#Дана матрица размера N*M . Для каждой строки матрицы с нечетным
#номером (1, 3,…) найти среднее арифметическое ее элементов.

import numpy as np #Отличный способ сделать себе матрицу
from colorama import init, Fore, Back

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон

N = int(input("Введите число строк матрицы: "))
M = int(input("Введите число столбцов матрицы: "))
print(Back.YELLOW + "\n")

def array() : #Функция заполняющая рандомными числами матрицу
	matrix = np.random.randint(0, 50, size=(N, M))
	print("Полученная матрица:\n" + str(matrix))
	return(matrix)

def average(): #Ищем среднее арефметическое всех строк
	s = 0
	for i in range(N):
		s += matrix[i]
	return s/N

matrix = array()
average()
b = list(average())
del b[1::2] #Убираем четные элементы
print(Back.CYAN + "\n")
print("Среднее арифметическое элементов нечетных строк: " + str(b))