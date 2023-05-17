
import numpy as np

def game_score_v3(number) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """  
 
    predict_min = 1
    predict_max = 101
    
    count = 0
    predict_number = np.random.randint(1, 101)  

    while number != predict_number:
       
        if (predict_max - predict_min) < 2:
            break 
        count += 1
       

        if predict_number > number:  
            predict_max = predict_number
            predict_number = round((predict_min + predict_max) / 2)
        
        else:
            
            predict_min = predict_number
            predict_number = round((predict_min + predict_max) / 2)
   
    return count


def score_game(game_score_v3) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        game_score_v3([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=(1000))  
   
    for number in random_array:
        count_ls.append(game_score_v3(number))
        score = int(np.mean(count_ls))
   
    return score


print(score_game(game_score_v3))