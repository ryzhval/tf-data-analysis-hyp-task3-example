import pandas as pd
import numpy as np
from scipy import stats

chat_id = 371649437 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:

    alpha = 0.01
    
    p_value = stats.permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
                 vectorized=True, 
                 n_resamples=5000,
                 alternative='greater').pvalue 
    return p_value < alpha
    return pvalue <= alpha
    
    
