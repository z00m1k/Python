#43. Дан массив размера N. Найти номера двух ближайших элементов из этого
#массива (то есть элементов с наименьшим модулем разности) и вывести эти
#номера в порядке возрастания.
import numpy as np #Отличный способ сделать себе матрицу
from colorama import init, Fore, Back

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон

def array() : #Функция заполняющая рандомными числами матрицу
	array = np.random.randint(0, 50, size=(N))
	print("Полученный массив:\n" + str(array))
	return(list(array))

def search() :
	min = abs(array[0] - array[1])
	I, J = 0, 1
	j = 1
	for i in range(N - 1):
		for j  in range (N):
			j = i + 1
			if abs(array[i] - array[j]) > abs(min):
				min = abs(array[i] - array[j])
				I, J = i, j
	if abs(array[N - 2] - array[N - 1]) > abs(min):
		min = abs(array[i] - array[j])
		I, J = i, j
	print("Наименьший модуль разности:", min)
	return(I, J)

N = int(input("Введите размер массива: "))
if N < 2:
	print("N не может быть меньше 2.")
	exit()

print(Back.YELLOW + "\n")

array = array()

print(Back.CYAN + "\n")

x = search()

print("Индексы двух ближайших элементов с наименьшим модулем разности:",x)


