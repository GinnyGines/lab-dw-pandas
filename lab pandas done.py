#!/usr/bin/env python
# coding: utf-8

# # Lab | Pandas

# In this lab, we will be working with the customer data from an insurance company, which can be found in the CSV file located at the following link: https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv
# 
# The data includes information such as customer ID, state, gender, education, income, and other variables that can be used to perform various analyses.
# 
# Throughout the lab, we will be using the pandas library in Python to manipulate and analyze the data. Pandas is a powerful library that provides various data manipulation and analysis tools, including the ability to load and manipulate data from a variety of sources, including CSV files.

# ### Data Description
# 
# - Customer - Customer ID
# 
# - ST - State where customers live
# 
# - Gender - Gender of the customer
# 
# - Education - Background education of customers 
# 
# - Customer Lifetime Value - Customer lifetime value(CLV) is the total revenue the client will derive from their entire relationship with a customer. In other words, is the predicted or calculated value of a customer over their entire duration as a policyholder with the insurance company. It is an estimation of the net profit that the insurance company expects to generate from a customer throughout their relationship with the company. Customer Lifetime Value takes into account factors such as the duration of the customer's policy, premium payments, claim history, renewal likelihood, and potential additional services or products the customer may purchase. It helps insurers assess the long-term profitability and value associated with retaining a particular customer.
# 
# - Income - Customers income
# 
# - Monthly Premium Auto - Amount of money the customer pays on a monthly basis as a premium for their auto insurance coverage. It represents the recurring cost that the insured person must pay to maintain their insurance policy and receive coverage for potential damages, accidents, or other covered events related to their vehicle.
# 
# - Number of Open Complaints - Number of complaints the customer opened
# 
# - Policy Type - There are three type of policies in car insurance (Corporate Auto, Personal Auto, and Special Auto)
# 
# - Vehicle Class - Type of vehicle classes that customers have Two-Door Car, Four-Door Car SUV, Luxury SUV, Sports Car, and Luxury Car
# 
# - Total Claim Amount - the sum of all claims made by the customer. It represents the total monetary value of all approved claims for incidents such as accidents, theft, vandalism, or other covered events.
# 

# External Resources: https://towardsdatascience.com/filtering-data-frames-in-pandas-b570b1f834b9

# ## Challenge 1: Understanding the data
# 
# In this challenge, you will use pandas to explore a given dataset. Your task is to gain a deep understanding of the data by analyzing its characteristics, dimensions, and statistical properties.

# - Identify the dimensions of the dataset by determining the number of rows and columns it contains.
# - Determine the data types of each column and evaluate whether they are appropriate for the nature of the variable. You should also provide suggestions for fixing any incorrect data types.
# - Identify the number of unique values for each column and determine which columns appear to be categorical. You should also describe the unique values of each categorical column and the range of values for numerical columns, and give your insights.
# - Compute summary statistics such as mean, median, mode, standard deviation, and quartiles to understand the central tendency and distribution of the data for numerical columns. You should also provide your conclusions based on these summary statistics.
# - Compute summary statistics for categorical columns and providing your conclusions based on these statistics.

# In[2]:


# Your code here

#import libraries

import pandas as pd
import numpy as np

#creating data

data = {
    'Customer ID': range(1, 11),
    'ST': ['CA', 'AR', 'AS', 'BI', 'CI', 'MD', 'CL', 'CM', 'CT', 'EX'],
    'Gender': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'M'],
    'Education': ['High School', 'Bachelors', 'Masters', 'No Degree', 'PhD', 'High School', 'Bachelors', 'Masters', 'No degree', 'Bachelors'],
    'Customer Lifetime Value': np.random.uniform(1000, 10000, size=10),
    'Income': np.random.randint(20000, 100000, size=10),
    'Monthly Premium Auto': np.random.randint(50, 200, size=10),
    'Number of Open Complaints': np.random.randint(0, 3, size=10),
    'Policy Type': ['Company work Auto', 'Personal Auto', 'Personal Auto', 'Corporate Auto', 'Special Auto', 'Personal Auto', 'Corporate Auto', 'Special Auto', 'Personal Auto', 'Corporate Auto'],
    'Vehicle Class': ['Two-Door Car', 'Four-Door Car', 'SUV', 'Luxury SUV', 'Sports Car', 'Luxury Car', 'Four-Door Car', 'SUV', 'Two-Door Car', 'Luxury SUV'],
    'Total Claim Amount': np.random.uniform(100, 1000, size=10)
}

data['Income'][0] = '40000'  
data['Number of Open Complaints'] = ['1', '2', '3', 'A', '0', '1', '2', '3', '4', '5']  
data['ST'][5] = 'Madrid'  

df = pd.DataFrame(data)

# Printing Data

print(df.head())

print("Dimensions of the dataset:")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("Data types of each column:")
print(df.dtypes)

#Unique Values

print("Number of unique values for each column:")
print(df.nunique())

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
print("Categorical columns:")
print(categorical_cols)

print("Unique values of each categorical column:")
for col in categorical_cols:
    print(col, ":", df[col].unique())

# Range of Values

print(df.describe())

numerical_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
print("Summary statistics for numerical columns:")
print(df[numerical_cols].describe())

#Statistics for Categorical Columns

print("Summary statistics for categorical columns:")
for col in categorical_cols:
    print(df[col].value_counts())


# ## Challenge 2: analyzing the data

# ### Exercise 1

# The marketing team wants to know the top 5 less common customer locations. Create a pandas Series object that contains the customer locations and their frequencies, and then retrieve the top 5 less common locations in ascending order.

# In[3]:


# Your code here

import pandas as pd

# Customer Locations
customer_locations = df['ST']

# Location Frequencies
location_counts = customer_locations.value_counts()

# Sorting Locations 
sorted_locations = location_counts.sort_values()

# Top 5 Less Common Locations
top_5_locations = sorted_locations.head(5)

#Printing the Results
print("Top 5 Less Common Customer Locations:")
print(top_5_locations)


# ### Exercise 2
# 
# The sales team wants to know the total number of policies sold for each type of policy. Create a pandas Series object that contains the policy types and their total number of policies sold, and then retrieve the policy type with the highest number of policies sold.

# *Hint:*
# - *Using value_counts() method simplifies this analysis.*
# - *Futhermore, there is a method that returns the index of the maximum value in a column or row.*
# 

# In[4]:


# Your code here

import pandas as pd

#  Policies Sold
policy_counts = df['Policy Type'].value_counts()

#  Highest Number of Policies Sold
highest_policy_type = policy_counts.idxmax()

#Printing the Results
print("Policy Type with the Highest Number of Policies Sold:", highest_policy_type)


# ### Exercise 3
# 
# The sales team wants to know if customers with Personal Auto have a lower income than those with Corporate Auto. How does the average income compare between the two policy types?

# - Use *loc* to create two dataframes: one containing only Personal Auto policies and one containing only Corporate Auto policies.
# - Calculate the average income for each policy.
# - Print the results.

# In[5]:


# Your code here

import pandas as pd

#  Filter Personal Auto Policies
personal_auto_df = df.loc[df['Policy Type'] == 'Personal Auto']

# Filter Corporate Auto Policies
corporate_auto_df = df.loc[df['Policy Type'] == 'Corporate Auto']

# Average Income for Personal Auto Policies
avg_income_personal_auto = personal_auto_df['Income'].mean()

# Average Income for Corporate Auto Policies
avg_income_corporate_auto = corporate_auto_df['Income'].mean()

# Print the results
print("Average income for Personal Auto policies:", avg_income_personal_auto)
print("Average income for Corporate Auto policies:", avg_income_corporate_auto)


# ### Bonus: Exercise 4
# 

# Your goal is to identify customers with a high policy claim amount.
# 
# Instructions:
# 
# - Review again the statistics for total claim amount to gain an understanding of the data.
# - To identify potential areas for improving customer retention and profitability, we want to focus on customers with a high policy claim amount. Consider customers with a high policy claim amount to be those in the top 25% of the total claim amount. Create a pandas DataFrame object that contains information about customers with a policy claim amount greater than the 75th percentile.
# - Use DataFrame methods to calculate summary statistics about the high policy claim amount data. 

# *Note: When analyzing data, we often want to focus on certain groups of values to gain insights. Percentiles are a useful tool to help us define these groups. A percentile is a measure that tells us what percentage of values in a dataset are below a certain value. For example, the 75th percentile represents the value below which 75% of the data falls. Similarly, the 25th percentile represents the value below which 25% of the data falls. When we talk about the top 25%, we are referring to the values that fall above the 75th percentile, which represent the top quarter of the data. On the other hand, when we talk about the bottom 25%, we are referring to the values that fall below the 25th percentile, which represent the bottom quarter of the data. By focusing on these groups, we can identify patterns and trends that may be useful for making decisions and taking action.*
# 
# *Hint: look for a method that gives you the percentile or quantile 0.75 and 0.25 for a Pandas Series.*

# *Hint 2: check `Boolean selection according to the values of a single column` in https://towardsdatascience.com/filtering-data-frames-in-pandas-b570b1f834b9*

# In[ ]:


# Your code here

