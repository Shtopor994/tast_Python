# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print ('Введите координаты:')
X = int(input('Х: '))
Y = int(input('Y: '))

if(X > 0 and Y > 0):
    result = 1
elif (X < 0 and Y > 0):
    result = 2
elif (X < 0 and Y < 0):
  result = 3
elif (X > 0 and Y < 0):
   result = 4
print(f'Точка с координатами {X} и {Y} находится в {result} четверти')

