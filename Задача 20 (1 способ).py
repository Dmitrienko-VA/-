# -*- coding: utf-8 -*-
from itertools import *
from time import time


def rebus_sum(string_1,string_2,string_3):
	if len(set(string_1+string_2+string_3))<=10: 
		string_1=string_1.lower()
		string_2=string_2.lower()
		string_3=string_3.lower()
		string=string_1+string_2+string_3
		d1=len(string_1) #длина первого слова
		d2=len(string_2) #длина второго слова
		d3=len(string_3) #длина третьего слова
		d=len(string) #длина трех слов
		if d3>=d1 and d3>=d2 and d3<=max(d1,d2)+1:
			m=[] #массив для хранения цифр подходящих особым условиям(ниже)
			for u in range(0,d): #заполняем массив
				m.append(-1)
			k=[1,2,3,4,5,6,7,8,9,0] #варианты для цифр
			if d1<d3 and d2<d3: #если длина суммы больше каждого из слагаемых, то сумма начинается с 1
				m[d1+d2]=1
				for l in range(0,d):
					if string[l]==string[d1+d2]:
						m[l]=m[d1+d2]
				k.remove(1)
			if string[d1-1]==string[d-1] and string[d1+d2-1]!=string[d-1]: #проверка на окончание нулем второго слова
				m[d1+d2-1]=0
				for l in range(0,d):
					if string[l]==string[d1+d2-1]:
						m[l]=m[d1+d2-1]
				k.remove(0)
			if string[d1+d2-1]==string[d-1] and string[d1-1]!=string[d-1]: #проверка на окончание нулем первого слова
				m[d1-1]=0
				for l in range(0,d):
					if string[l]==string[d1-1]:
						m[l]=m[d1-1]
				k.remove(0)
			if string[d1-1]==string[d1+d2-1]==string[d-1]: #проверка что все числа оканчаются на 0
				m[d-1]=0
				for l in range(0,d):
					if string[l]==string[d-1]:
						m[l]=m[d-1]
				k.remove(0)
			for array_of_values in permutations(k):
				counter=0#счетчик для передвижения по массиву вариантов
				mas=[] #массив в котором будут храниться цифры чисел по порядку
				for q in range(0,d):
					mas.append(m[q]) #копируем массив который прошел особые условия
				for i in range(0,d):#заполняем массив
					if mas[i]==-1:
						for j in range(0,d):
							if string[j] == string[i]:#ищем одинаковые буквы
								mas[j] = array_of_values[counter]
						mas[i] = array_of_values[counter]
						counter=counter+1
				number_1=0 #собираем первое число
				for ind1 in range(0,d1):
					number_1=number_1+mas[-1-ind1-d+d1]*10**ind1
				number_2=0 #собираем второе число
				for ind2 in range(0,d2):
					number_2=number_2+mas[-1-ind2-d+d1+d2]*10**ind2
				number_3=0 #собираем третье число
				for ind3 in range(0,d3):
					number_3=number_3+mas[-1-ind3]*10**ind3
				if number_1//10**(d1-1)!=0 and number_2//10**(d2-1)!=0 and number_3//10**(d3-1)!=0:
					if number_1+ number_2== number_3:
							return [number_1,number_2,number_3]
	return 'Solution does not exist'



def test():
	str_1='два'
	str_2='три'
	str_3='пять'
	if(rebus_sum(str_1,str_2,str_3)==[236,849,1085]):
		print('test_for_solvable: true')
	else:
		print('test_for_solvable: false')
	str_1='tt'
	str_2='t'
	str_3='ttt'
	if(rebus_sum(str_1,str_2,str_3)=='Solution does not exist'):
		print('test_for_unsolvable: true')
	else:
		print('test_for_unsolvable: false')



#Проверка функции
print('ЗАДАЧА 20: Написать программу решения математических ребусов, в которых зашифровано сложение. Написать программу, которая получает на входе математический ребус в виде трех слов и возвращает числа, которые были представлены этими словами, или сообщает о невозможности решения.')
print('')
test()
flag='Yes'
while flag=='Yes':
	word_1=input('Enter word_1 = ')
	word_2=input('Enter word_2 = ')
	word_3=input('Enter word_3 = ')
	tic=time()
	print(rebus_sum(word_1,word_2,word_3))
	toc=time()
	print('Algorithm execution time:  ',toc - tic)
	flag=input('Start a new rebus (Yes/No) : ')

#Примеры:
#два+три=пять
#лиса+волк=звери
#драма+драма=театр
# кот+кто=ток
#синица+синица=птички
