import math 
from scipy.stats import norm
p = 0.9
q = 1-p
seats = 300
confidence_level = 0.99
# Calculate the z-score for the confidence level
z_score = norm.ppf(confidence_level)

def find_optimal(p , seats , z_critical) :
    n =  math.ceil((seats + z_critical * math.sqrt(p * q * seats)) / p)
    return n

n = find_optimal(p , seats ,z_score)
print(f'la valeur est p(S_n < {seats}) >= {confidence_level} est {n}')






