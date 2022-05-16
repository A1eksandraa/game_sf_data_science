"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно загадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    mn_num = 0
    mx_num = 100
    predict_number = np.random.randint(1, 101)  # предполагаемое число

    while True:
        count += 1
        if number < predict_number:
            mx_num = predict_number - 1
            predict_number = (mx_num + mn_num) // 2  
        elif number > predict_number:
            mn_num = predict_number + 1
            predict_number = (mx_num + mn_num) // 2
        else:
            break  # выход из цикла если угадали
    return count



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает на алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls =[] #список длясохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101,size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score

#RUN
if __name__ == "__main__":
    score_game(random_predict)