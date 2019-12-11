#Дана матрица размера N*M (M и N – четные числа). Поменять местами
#левую нижнюю и правую верхнюю четверти матрицы.
import numpy as np #Отличный способ сделать себе матрицу
from colorama import init, Fore, Back

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон

N = int(input("Введите число строк матрицы: "))
M = int(input("Введите число столбцов матрицы: "))
if (N %2 != 0 ) or (M %2 != 0):
	print("\nЧисла должы быть четными!")
	exit()
print(Back.YELLOW + "\n")

def array() : #Функция заполняющая рандомными числами матрицу
	matrix = np.random.randint(0, 50, size=(N, M))
	print("Полученная матрица:\n" + str(matrix))
	return(list(matrix))

matrix = array()
print(Back.CYAN + "\n")
print("Отражение матрицы по горизонтали относительно середины:")
for i in zip(*matrix):
	print(i)
