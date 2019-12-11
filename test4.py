#34. Дана целочисленная матрица размера N*M . Найти элемент, являющийся
#максимальным в своей строке и минимальным в своем столбце. Если такой
#элемент отсутствует, то вывести 0.

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


def sedl() : #Поиск и вывод седловой точки с помощью библиотеки numpy

	min_str = np.max(matrix, axis=1)
	min_str_idx = np.argmin(min_str)
 
	max_col = np.min(matrix, axis=0)
	max_col_idx = np.argmax(max_col)
	if np.argmax(matrix[min_str_idx, :]) == max_col_idx and np.argmin(matrix[:, max_col_idx]) == min_str_idx:
		print ("Седловая точка =", matrix[min_str_idx][max_col_idx],"\nИ имеет координаты: [", min_str_idx,"][", max_col_idx,"]")
	else:
		print ("Седловой точки нет =>", 0)

matrix = array()
print(Back.CYAN + "\n")
sedl()