from scipy.stats import t
import numpy as np

alpha = 0.05
n = 72  # sample size
df = n - 2 #degrees of freedom

t_crit = t.ppf(1 - alpha/2, df) # critical value
r_crit = np.sqrt(t_crit**2 / (t_crit**2 + df))

print("Critical value of Pearson r:", r_crit)
