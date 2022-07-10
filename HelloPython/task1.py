# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:* 
    
#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет

#num1, num2 = int(input()), int(input())
#if num1**2 == num2 or num2**2 == num1:
#    print(num1, num2, '-> yes')
#else:
#    print(num1, num2, '-> no')


# num1, num2, num3, num4, num5 = int(input()), int(input()), int(input()), int(input()), int(input())
# temp = 0
# if num1>temp:
#     temp=num1
# if num2>temp:
#     temp=num2
# if num3>temp:
#     temp=num3
# if num4>temp:
#     temp=num4
# if num5>temp:
#     temp=num5
# print(temp)

# lst = [1,9,5,6,0]
# max = lst[0]
# for item in lst:
#     if max < item:
#         max=item
# print(max)

# Дано значение температуры в градусах Цельсия. Вывести температуру  в градусах Фаренгейта. 

# a = float(input("Введите температуру в Цельсиях: ")) 

# farengeit = float(a*1.8)+32 

# print(f'Температура по Фаренгейту: {farengeit}')

# n = int(input('enter the number ' ))
# x = n * (-1)
# while x <= n:
#     print(x) 
#     x+=1

# import math
# number2 = float(input("Enter number : "))

# result = math.floor(number2 % math.floor(number2)*10)

# if result == 0:
#     print(f"{number2} - > нет")
# else :
#     print(f"{number2} - > {result}")

n = float(input('введите число:   '))
if n%1 == 0:
    print ('нет')
else:
 n1=int(n%1*10)
 print(n1)

