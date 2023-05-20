# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# %%
data = pd.read_csv('Islander_data.csv')

# %% [markdown]
# Q1.

# %%
corr = data['age'].corr(data['Diff'])
print("Correlation between Age and Diff: ", corr)

# %% [markdown]
# Q2.

# %%
n_samples = 10000
sample_size = 20
metric = 'mean'


sample_means = np.zeros(n_samples)


for i in range(n_samples):
    samples = np.random.choice(data['Diff'], size=sample_size, replace=False)
    sample_means[i] = np.mean(samples)


mean_sample_means = np.mean(sample_means)
std_sample_means = np.std(sample_means, ddof=1)


std_error = std_sample_means / np.sqrt(sample_size)


print(f"The standard error is {std_error}")

# %% [markdown]
# Q3.

# %%
number_of_samples = 10000
size_of_sample = 20

bootstrap_sample_means = np.empty(number_of_samples)

for i in range(number_of_samples):
    bootstrap_sample = np.random.choice(data['Diff'], size=size_of_sample, replace=True)
    bootstrap_sample_means[i] = np.mean(bootstrap_sample)

confidence_interval = np.percentile(bootstrap_sample_means, [2.5, 97.5])
lower_limit, upper_limit = confidence_interval

print("Lower Limit: ", lower_limit)
print("Upper Limit: ", upper_limit)


# %% [markdown]
# Q4.

# %%
contingency_table = pd.crosstab(data['Happy_Sad_group'], data['Drug'])


# %%
count = contingency_table.loc['S', 'A']
print(count)

# %% [markdown]
# Q5.

# %%
from scipy.stats import chi2_contingency

chi2_stat, p_value, dof, expected_freqs = chi2_contingency(contingency_table)

print("Chi-square value:", chi2_stat)
print("p-value:", p_value)


# %%
print(chi2_stat + p_value)

# %% [markdown]
# Q6.

# %%
row_totals = contingency_table.sum(axis=1)
col_totals = contingency_table.sum(axis=0)
total = contingency_table.sum().sum()
expected_frequencies = np.outer(row_totals, col_totals) / total


observed = contingency_table.loc['H', 'T']
expected = expected_frequencies[0, 2]
pearson_residual = (observed - expected) / np.sqrt(expected * (1 - col_totals[2] / total) * (1 - row_totals[0] / total))


print(f"The Pearson residual for Happy (H) subjects who are given drug T is {pearson_residual}")

# %% [markdown]
# Q7.

# %%
def chi_squared_permutation_test(contingency_table, num_permutations=10000):
    observed_chi2, _, _, _ = chi2_contingency(contingency_table)


    chi2_permutations = []
    for i in range(num_permutations):
        shuffled_labels = np.random.permutation(data["Happy_Sad_group"])
        shuffled_table = pd.crosstab(shuffled_labels, data["Drug"])
        chi2, _, _, _ = chi2_contingency(shuffled_table)
        chi2_permutations.append(chi2)
    p_value = (np.sum(chi2_permutations >= observed_chi2) ) / (num_permutations )


    return observed_chi2, p_value


observed_chi2, p_value = chi_squared_permutation_test(contingency_table, num_permutations=10000)
print(f"The p-value is {p_value}")


