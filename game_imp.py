import numpy as np

def random_predict_imp(number:int=1) -> int:

    count = 0   #переменная для подсчета кол-ва попыток
    np.random.seed(1)
    l, r = 1, 101   #задаем начальные границы угадывания

    while True:
        count += 1
        predict_number = np.random.randint(l, r)
        if predict_number > number:     #если наше число больше исходного, то сдвигаем правую границу
            r = predict_number          #т. к. правее уже нет смысла искать
        else:
            l = predict_number          #иначе сдвигаем левую границу
        if number == predict_number:
            break
    return(count)

def score_game_imp(random_predict_imp):
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_imp(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game_imp(random_predict_imp)