# '''Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.
# Посмотрели, что такое множество? Вот здесь его не используйте'''

import random

def findNumberInList(list_of_numbers):
    List = []
    for number in list_of_numbers:
        if number not in List:
            List.append(number)
    return List


numbersList = []
for i in range(1, 20): 
    numbersList.append(random.randint(1, 10))

print(numbersList)
print(findNumberInList(numbersList)) 