# %% [markdown]
# ### AKSHAY | 202051018
# ### Assignment 8
# ### CS 312 : Data Analytics and Visualization

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# %%
data = pd.read_csv("weight-height.csv")

# %%
print(data.head())

# %% [markdown]
# Q1: Verify the Central Limit Theorem using the ”Height” feature of the data.

# %%
# Extract the height column as a numpy array
heights = data['Height'].values

# Set the sample size and number of simulations
sample_size = 100
num_simulations = 10000

# Initialize an array to store the sample means
sample_means = np.zeros(num_simulations)

# Loop over the number of simulations
for i in range(num_simulations):
    # Randomly sample heights with replacement
    sample = np.random.choice(heights, size=sample_size, replace=True)
    # Calculate the sample mean
    sample_mean = np.mean(sample)
    # Store the sample mean
    sample_means[i] = sample_mean

# Plot the distribution of sample means
plt.hist(sample_means, bins=50, density=True, alpha=0.5)

# Plot the normal distribution with the same mean and variance
mu = np.mean(heights)
sigma = np.std(heights)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
y = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x - mu)**2/(2*sigma**2))
plt.plot(x, y)

plt.show()

# %% [markdown]
# Q2: Perform the Bootstrap on ”Height” feature of the data.

# %%
values=data["Height"].to_numpy()

# %%
number_of_samples=10000 # R times
size_of_sample=300  # n
sample_mean=[]
for i in range(number_of_samples):
    # Calulate mean for n samples
    sample_mean.append(np.mean(np.random.choice(values,size_of_sample,replace=True)))

# %%
_=plt.hist(sample_mean,bins=100)
plt.show()
standard_error=np.std(sample_mean)/math.sqrt(len(sample_mean))
print(standard_error)

# %% [markdown]
# Q3: Calculate the Confidence Interval of 95 % using sample means derived using Bootstrap

# %%
CI=0.95
sorted_means=np.sort(sample_mean)
l=len(sorted_means)
idx=math.floor(l*((1-CI)/2))

print("Lower level :", sorted_means[idx])
print("Upper level :", sorted_means[l-idx-1])


