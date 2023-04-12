import pandas as pd
import numpy as np
from scipy import stats
import math

chat_id = 371649437 # Ваш chat ID, не меняйте название переменной

def solution(control: np.array, test: np.array) -> bool:
    
     # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Ваш ответ, True или False
    alpha = 0.01
    
#     p1 = x_success / x_cnt
#     p2 = y_success / y_cnt
#     p_comb = (x_success + y_success) / (x_cnt + y_cnt)
#     difference = p1 - p2
 
#     z_value = difference / math.sqrt(
#         p_comb * (1 - p_comb) * (1 / x_success + 1 / y_success)
#     ) 
#     distr = stats.norm(0, 1)  
    
#     p_value = (1 - distr.cdf(abs(z_value))) * 2 
    
#     if (p_value < alpha):
#       return True
#     else: 
#       return False

    res = (stats.ks_2samp(control, test, alternative = 'two-sided').pvalue < alpha)
    return res
    
    
