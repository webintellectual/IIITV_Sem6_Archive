# %% [markdown]
# # Author © : Akshay | 202051018

# %% [markdown]
# Data Analytics & Visualisation | Assignment 6

# %%
import pandas as pd
import seaborn as sns
import math

# %% [markdown]
# Loading Dataset

# %%
data1 = pd.read_csv("primary_completion_rate_female.csv", skiprows=4)
df1 = data1.copy()
print(df1)

# %%
data2 = pd.read_csv("population_of_female.csv", skiprows=4)
df2 = data2.copy()
print(df2)

# %% [markdown]
# Q1. Create a column named “average_rate” in “primary_completion_rate_female.csv” that
# contains the average (over time) completion rate.

# %%
df1['average_rate'] = df1.mean(axis=1,numeric_only=True)

# %%
print(df1.head())

# %%
print(df1['average_rate'])

# %% [markdown]
# Q2. Create a column named “Latest Population” in “population_of_female.csv” that contains the
# latest population of females in the country.

# %%
df2["Latest Population"] = df2['2021']

# %%
print(df2.head())

# %%
print(df2['Latest Population'])

# %% [markdown]
# Q3. What is the weighted average of primary rates of different countries? The weight should be the
# Latest population of females in the country.

# %%
#  Weighted mean
tmp1=(df1["average_rate"]*df2["Latest Population"])
#print(tmp1)
tmp2=tmp1/df2["Latest Population"].sum()
weighted_mean=tmp2.sum()
print("weighted mean: ", weighted_mean)

# %% [markdown]
# Q4. What is the Median of average primary completion rate?

# %%
print("average primary completion rate: ", df1['average_rate'].median())

# %% [markdown]
# Q5. What is the InterQuartile Range of average primary completion rate?

# %%
IQR=df1["average_rate"].quantile(0.75)-df1["average_rate"].quantile(0.25)
print("IQR of average primary completion rate: ", IQR)

# %% [markdown]
# Q6. What is the Variance of average primary completion rate?

# %%
print("Variance of average primary completion rate: ", df1['average_rate'].var())


