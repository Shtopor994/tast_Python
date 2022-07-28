def filter_by_points(tuples_list):
    result_list = []
    result = 0
    for number, language in tuples_list:#range(len(), 0, -1)
        points = reduce(lambda a,b: a+b, [ord(char) for char in language])
        if points % number == 0:
            result += points
            result_list.append((points, language))
    del tuples_list
    return result, result_list

with open('candy-game\program_langs.txt', encoding='utf-8') as file:
        languages = file.read().split('\n')
    numbers = list(range(1, len(languages)+1))
    #tuples_list = enumerate([word.upper() for word in languages])
    tuples_list = zip(numbers, [word.upper() for word in languages])
    return list(tuples_list)
