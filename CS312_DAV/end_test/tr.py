

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from scipy.stats import norm
import pandas as pd
from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np
from scipy.stats import chi2
import math




# In[4]:




location = "Islander_data.csv"
df = pd.read_csv(location)



# #### Q1


# In[6]:




print(df.corr())




# #### Q2


# In[7]:




n_samples = 10000
sample_size = 20
metric = 'mean'


sample_means = np.zeros(n_samples)


for i in range(n_samples):
    samples = np.random.choice(df['Diff'], size=sample_size, replace=False)
    sample_means[i] = np.mean(samples)


mean_sample_means = np.mean(sample_means)
std_sample_means = np.std(sample_means, ddof=1)


std_error = std_sample_means / np.sqrt(sample_size)


print(f"The standard error is {std_error}")




# #### Q3


# In[10]:




number_of_samples = 10000
size_of_sample = 20
metric = 'mean'


sample_means = np.zeros(number_of_samples)
for i in range(number_of_samples):
    samples = np.random.choice(df['Diff'], size=size_of_sample, replace=True)
   
    sample_means[i] = np.mean(samples)


lower_limit, upper_limit = norm.interval(0.95, loc=np.mean(sample_means), scale=np.std(sample_means))


print(f"The 95% confidence interval is ({lower_limit}, {upper_limit})")




# #### Q4


# In[25]:




contingency_table = pd.crosstab(df['Happy_Sad_group'], df['Drug'])
sad_a_count = contingency_table.loc['S', 'A']


print(f"The count of Sad subjects who are given drug A is {sad_a_count}")




# #### Q5


# In[13]:




chi2, p, dof, expected = chi2_contingency(contingency_table)


sum_chi2_p = chi2 + p


print(f"The sum of chi-square value and p-value is {sum_chi2_p}")




# #### Q6


# In[22]:




row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)
total = contingency_table.sum().sum()
expected_frequencies = np.outer(row_totals, col_totals) / total


observed = contingency_table.loc['H', 'T']
expected = expected_frequencies[0, 2]
pearson_residual = (observed - expected) / np.sqrt(expected * (1 - col_totals[2] / total) * (1 - row_totals[0] / total))


print(f"The Pearson residual for Happy (H) subjects who are given drug T is {pearson_residual}")




# #### Q7


# In[27]:




# def chi_squared_permutation_test(contingency_table, num_permutations=10000):
#     observed_chi2, _, _, _ = chi2_contingency(contingency_table)


#     chi2_permutations = []
#     for i in range(num_permutations):
#         shuffled_labels = np.random.permutation(df["Happy_Sad_group"])
#         shuffled_table = pd.crosstab(shuffled_labels, df["Drug"])
#         chi2, _, _, _ = chi2_contingency(shuffled_table)
#         chi2_permutations.append(chi2)
#     p_value = (np.sum(chi2_permutations >= observed_chi2) ) / (num_permutations )


#     return observed_chi2, p_value


# observed_chi2, p_value = chi_squared_permutation_test(contingency_table, num_permutations=10000)
# print(f"The p-value is {p_value}")




# ##### P value is 1.0 which is greater than 0.05 (standard alpha)
# ##### this the data is not ligit
# ##### null hypothesis is true


# In[ ]:
