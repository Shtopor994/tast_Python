# '''Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]'''

from Func import inputNumbers

number = inputNumbers("Задайте натуральное число N: ")

def simpleNumber(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def denominator(num):
    denominatorsList = []
    for i in range(2, num):
        if num % i == 0 and simpleNumber(i): 
            denominatorsList.append(i)
    return denominatorsList


print(simpleNumber(number))
print(denominator(number)) 