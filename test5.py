#Дана матрица размера N*M. Найти максимальный среди минимальных
#элементов ее строк.

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


def minn() : #Поиск минимальной точки с помощью библиотеки numpy

	min_str = np.min(matrix, axis=1)
	min_str_idx = np.argmin(min_str)
	min_str_list = list(min_str)
	print("Минимальные элементы всех строк:", min_str_list)
	print("Максимальный элемент из минимальных:", max(min_str_list))

matrix = array()
print(Back.CYAN + "\n")
minn()