#15. Дан массив размера N и целые числа K и L ( 1 <= K <= L <= N ). Найти сумму
#элементов массива с номерами от K до L включительно и их количество.
import numpy as np #Отличный способ сделать себе матрицу
from colorama import init, Fore, Back

init()
print(Fore.BLACK)#Черный цвет
print(Back.GREEN)#Зеленый фон


def array() : #Функция заполняющая рандомными числами матрицу
	matrix = np.random.randint(0, 50, size=(N))
	print("Полученный массив:\n" + str(matrix))
	return(list(matrix))

def summa() :
	print(k)
	k1 = k
	print(matrix)
	array_sum = 0
	x = l - k1
	while k1 < l:
		array_sum += int(matrix[k1])
		k1 += 1
	return(array_sum, x)

N = int(input("Введите размер массива: "))
if N < 1:
	print("N не может быть меньше 1.")
	exit()
k = int(input("Введите переменную K: "))
if (k > N) or (k < 1):
	print("Переменна K не может принимать таких значений.")
	exit()
l = int(input("Введите переменную L: "))
if (l < k) or (l < 1):
	print("Переменна L не может принимать таких значений.")
	exit()

print(Back.YELLOW + "\n")

matrix = array()
print(Back.CYAN + "\n")
array_sum = summa()
#print("Сумма элементов массива с номерами от K до L :", array_sum[0])
#print("Количество элементов массива:", array_sum[1])

