from scipy import stats

# Example data (replace with actual values)
group1 = [12, 15, 14, 10, 13]
group2 = [22, 20, 19, 23, 21]
group3 = [30, 28, 29, 31, 27]

# Perform ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

print("F-statistic:", f_stat)
print("p-value:", p_value)
