#Дан массив размера N. Найти максимальный из его элементов, не
#являющихся ни локальным минимумом, ни локальным максимумом
#(локальный минимум – это элемент, который меньше любого из своих
#соседей; локальный максимум – это элемент, который больше любого из
#своих соседей). Если таких элементов в массиве нет, то вывести 0 (как
#вещественное число).
import numpy as np #Отличный способ сделать себе матрицу
from colorama import init, Fore, Back

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон

def array() : #Функция заполняющая рандомными числами матрицу
	array = np.random.randint(0, 100, size=(N))
	print("Полученный массив:\n" + str(array))
	return(list(array))

def search_min():
	el_min = []
	el_min_idx = []
	i = 1
	if array[-1] < array [-2]:
		el_min.append(array[-1])
	for i in range(N - 1):
		if (array[i - 1] > array [i]) and (array [i] < array[i + 1]):
			el_min.append(array[i])
	return(el_min)

def search_max():
	el_max = []
	el_max_idx = []
	i = 1
	if array [-1] > array [-2]:
		el_max.append(array[-1])
	for i in range(N - 1):
		if (array[i - 1] < array [i]) and (array [i] > array[i + 1]):
			el_max.append(array[i])
	return(el_max)

def filt():
	if (len(search) == (len(array))):
		print("None\n\n",float(0))
		exit()
	for i in range (len(search)):
		array.remove(search[i])
	return(max(array))

N = int(input("Введите размер массива: "))
if N < 1:
	print("N не может быть меньше 1.")
	exit()

print(Back.YELLOW + "\n")

array = array()

search_min, search_max = search_min(), search_max()

print(Back.CYAN + "\n")

search = search_min + search_max

print("Максимальный элемент не являющийся экстремумом:\n" + str(filt()))