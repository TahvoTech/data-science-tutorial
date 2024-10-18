import pandas as pd  # For data manipulation
import numpy as np   # For numerical operations
import seaborn as sns  # For creating statistical visualizations
import matplotlib.pyplot as plt  # For plotting

# Load the Titanic dataset from the 'titanic3.csv' file into a Pandas DataFrame
data = pd.read_csv('titanic3.csv')

# Create a figure with 5 subplots in a row and set the figure size to 30x5 inches
fig, axs = plt.subplots(ncols=5, figsize=(30,5))

# Create a violin plot showing the age distribution of survivors and non-survivors, split by sex
sns.violinplot(x="survived", y="age", hue="sex", data=data, ax=axs[0])

# Create point plots to visualize relationships between survival status and other variables, split by sex
# Point plot for siblings/spouses aboard vs survival status
sns.pointplot(x="sibsp", y="survived", hue="sex", data=data, ax=axs[1])

# Point plot for parents/children aboard vs survival status
sns.pointplot(x="parch", y="survived", hue="sex", data=data, ax=axs[2])

# Point plot for passenger class vs survival status
sns.pointplot(x="pclass", y="survived", hue="sex", data=data, ax=axs[3])

# Create a violin plot showing the fare distribution of survivors and non-survivors, split by sex
sns.violinplot(x="survived", y="fare", hue="sex", data=data, ax=axs[4])

# Show the plots
plt.show()

# Replace 'male' with 1 and 'female' with 0 in the 'sex' column for easier numeric processing
data.replace({'male': 1, 'female': 0}, inplace=True)

# Calculate and print the correlation between 'survived' and other numeric columns
# The 'numeric_only=True' argument ensures that only numeric columns are included in the correlation calculation
# .abs() returns the absolute values of the correlations
print(data.corr(numeric_only=True).abs()[["survived"]])

# Create a new column 'relatives' that equals 1 if the passenger has relatives aboard (either siblings/spouses or parents/children), 0 otherwise
data['relatives'] = data.apply(lambda row: int((row['sibsp'] + row['parch']) > 0), axis=1)

# Calculate and print the correlation again, including the newly created 'relatives' column
print(data.corr(numeric_only=True).abs()[["survived"]])

# If you want to skip unnecessary columns (e.g., the 'body' column), select specific columns to include in the correlation calculation

# Create the 'relatives' column again to ensure it's up to date
data['relatives'] = data.apply(lambda row: int((row['sibsp'] + row['parch']) > 0), axis=1)

# List of columns you want to include in the correlation analysis, skipping unnecessary ones like 'body'
columns_to_check = ['pclass', 'survived', 'sex', 'age', 'sibsp', 'parch', 'fare', 'relatives']

# Calculate the correlation matrix for the specified columns
corr_matrix = data[columns_to_check].corr()

# Extract and print the absolute correlation values for the 'survived' column
corr_with_survived = corr_matrix[['survived']].abs()
print(corr_with_survived)
