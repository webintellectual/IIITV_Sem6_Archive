# %% [markdown]
# Loading modules

# %%

import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
import numpy as np

# %% [markdown]
# Loading data

# %%
data = pd.read_csv("cookie_cats.csv")

# %%
print(data)

# %% [markdown]
# Checking types of columns

# %%
print(data.dtypes)

# %% [markdown]
# ##### Q1. Check which version of the game is better by computing average ”sum gamerounds”.

# %%
# Computing the mean of sum_gamerounds for each version
mean_gamerounds = data.groupby('version')['sum_gamerounds'].mean()
print(mean_gamerounds)

# %%
# Print the version with the highest mean of sum_gamerounds
if mean_gamerounds['gate_30'] > mean_gamerounds['gate_40']:
    print("Version gate_30 is better with a mean of", mean_gamerounds['gate_30'], "sum_gamerounds")
else:
    print("Version gate_40 is better with a mean of", mean_gamerounds['gate_40'], "sum_gamerounds")

# %% [markdown]
# The version with a higher mean of "sum_gamerounds" can be considered better in terms of engagement.
# So, Answer is: gate_30 version

# %% [markdown]
# ##### Q2. To check that the difference in average of ”sum gamerounds” is by chance or it is a real difference, perform the permutation Resampling on the data and derive the probability. Make the decision based on derived probability.

# %%
# Compute the observed difference in means between the two versions
obs_diff = data.groupby('version')['sum_gamerounds'].mean().diff()[1]

# Combine the data from both versions
combined_data = data['sum_gamerounds'].values

# Initialize an empty list to store the resampled differences in means
resampled_diffs = []

# Set the random seed for reproducibility
np.random.seed(42)

# Perform permutation resampling and compute the differences in means
for i in range(10000):
    np.random.shuffle(combined_data)
    group1 = combined_data[:len(data)//2]
    group2 = combined_data[len(data)//2:]
    resampled_diff = np.mean(group1) - np.mean(group2)
    resampled_diffs.append(resampled_diff)

# Compute the probability of obtaining a difference as extreme as or more extreme than the observed difference
p_value = (np.abs(resampled_diffs) >= np.abs(obs_diff)).mean()

# Print the probability
print("The probability of obtaining a difference in means as extreme as or more extreme than the observed difference by chance is:", p_value)


# %% [markdown]
# A p-value of 0.477 indicates that there is a high probability (47.7%) of observing a difference in means as extreme as or more extreme than the observed difference between the two versions by chance, under the assumption that there is no true difference between the versions.


