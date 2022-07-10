# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
from turtle import distance
from unittest import result

print ('Введите координаты точки А:')
X1 = int(input('Х1: '))
Y1 = int(input('Y1: '))

print ('Введите координаты точки B:')
X2 = int(input('Х2: '))
Y2 = int(input('Y2: '))

distance = math.sqrt((X2 - X1) * (X2 - X1) + (Y2 - Y1) * (Y2 - Y1)) 
print(round(distance, 3))