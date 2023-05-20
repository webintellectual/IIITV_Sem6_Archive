# %% [markdown]
# ## AKSHAY | 202051018
# ## Assignment 7
# ## CS/IT 312 : Data Analytics and Visualization

# %%
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
import seaborn as sns

# %%
data=pd.read_csv("weight-height.csv")
population_mean = round(data['Height'].mean(),3)
print("Population mean: ", population_mean)
print(data)

# %% [markdown]
# 1. Perform Random Sampling by choosing 1000 samples from data. Compute the sample mean and population mean (from whole data) and then compute the error between both mean.

# %%
simple_random_sample = data.sample(n=1000).sort_index()
print(simple_random_sample)

# %%
simple_random_mean = round(simple_random_sample['Height'].mean(),3)
print("Sample mean: ", simple_random_mean)

# %%
simple_random_sample_error = abs(population_mean-simple_random_mean)
print("Random Sampling Error: ", simple_random_sample_error)

# %% [markdown]
# 2. Perform Systematic Sampling by choosing 1000 samples from data. Compute the sample mean and population mean (from whole data) and then compute the error between both mean.

# %%
def systematic_sampling(df, step):
    
    indexes = np.arange(0,len(df),step=step)
    systematic_sample = df.iloc[indexes]
    return systematic_sample
    
# Obtain a systematic sample and save it in a new variable
systematic_sample = systematic_sampling(data, 10)
print("Systematic sample size: ", len(systematic_sample))
print(systematic_sample)

# %%
# Save the sample mean in a separate variable
systematic_mean = round(systematic_sample['Height'].mean(),3)
print("Systematic sample mean: ", systematic_mean)

# %%
systematic_sample_error = abs(population_mean-systematic_mean)
print("Systematic Sampling Error: ", systematic_sample_error)

# %% [markdown]
# 3. Perform Stratified Sampling by choosing 1000 samples from data. Compute the sample mean and population mean (from whole data) and then compute the error between both mean.

# %%
# Set the split criteria
split = StratifiedShuffleSplit(n_splits=1, test_size=1000)


# Perform data frame split
for x, y in split.split(data, data['Gender']):
    stratified_random_sample = data.iloc[y]

# View sampled data frame
print("Sample size: ", len(stratified_random_sample))
print(stratified_random_sample)

# %%
stratified_random_sample_mean = round(stratified_random_sample['Height'].mean(),3)
print(stratified_random_sample_mean)

# Obtain the sample mean for each group
stratified_random_sample.groupby("Gender").mean()
print(stratified_random_sample)

# %%
stratified_random_sample_error = abs(population_mean-stratified_random_sample_mean)
print("Stratified Sampling Error: ", stratified_random_sample_error)


