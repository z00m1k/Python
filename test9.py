#Дан массив A размера N и целое число K ( 1 <= K <= N ). Вывести элементы
#массива с порядковыми номерами, кратными K: AK, A2·K, A3·K, … .

import numpy as np #Отличный способ сделать себе матрицу
from colorama import init, Fore, Back

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон

def array() : #Функция заполняющая рандомными числами матрицу
	array = np.random.randint(0, 50, size=(N))
	print("Полученный массив:\n" + str(array))
	return(list(array))

def search():
	search = []
	for i in range(N):
		if (i %K == 0):
			search.append(array[i])
	return(search)



N = int(input("Введите размер массива: "))
if N < 1:
	print("N не может быть меньше 1.")
	exit()
K = int(input("Введите переменную K: "))
if (K > N) or (K < 1):
	print("Переменна K не может принимать таких значений.")
	exit()

print(Back.YELLOW + "\n")

array = array()

search = search()

print(Back.CYAN + "\n")

print(search)