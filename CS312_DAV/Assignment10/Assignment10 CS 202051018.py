# %% [markdown]
# ### CS/IT 312 : Data Analytics and Visualization
# ### Assignment 10 | AKSHAY | 202051018

# %%
import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

# %%
data1 = pd.read_csv('cookie_cats.csv')

# %%
cookie_cats = pd.read_csv('cookie_cats.csv')

# Split the data into two groups based on gate level
gate_30 = cookie_cats[cookie_cats['version'] == 'gate_30']['sum_gamerounds']
gate_40 = cookie_cats[cookie_cats['version'] == 'gate_40']['sum_gamerounds']

# Perform a two-sample t-test
t_stat, p_val = ttest_ind(gate_30, gate_40, equal_var=True)

# Print the results
print('t-statistic:', t_stat)
print('p-value:', p_val)

# %%
if p_val < 0.05:
    print("""We can conclude that the difference we observed between the groups is not due to chance and 
    is likely due to some underlying factor, such as the level at which the gate was presented to users.""")
else:
    print("""The observed difference between the groups may be due to chance or random variation, 
    and we cannot confidently conclude that it is due to the level at which the gate was presented.""")

# %%
data2 = pd.read_csv('IPL_Auction_2022_FullList.csv')

# %%
# Create contingency table for Specialism vs Batting
contingency_table = pd.crosstab(data2['Specialism'], data2['Batting'])

# Print the contingency table
print(contingency_table)

# %%
# Perform chi-square test on the contingency table
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the test results
print('Chi-square statistic:', chi2)
print('P-value:', p_value)
print('Degrees of freedom:', dof)
print('Expected values:', expected)


