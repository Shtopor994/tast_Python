#2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             result = not x and not y and not z
#             result2 = not (x or y or z)
#             print(x,y,z,'  ', result, '   ', result2)
# if result == result2:
#     print('равенство истинно')
# else:
#     print ('равенство ложно')

print ('\nX \t Y \t Z \t ¬(X ⋁ Y ⋁ Z) \t ¬X ⋀ ¬Y ⋀ ¬Z \t ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \n')
for x in range(2):
    for y in range(2):
        for z in range(2):
            on_left = not(x or y or z)
            on_right = not(x) and not(y) and not (z)
            print(
                f'{x} \t {y} \t {z}  \t  {on_left}  \t  {on_right}  \t  {on_left == on_right}')
