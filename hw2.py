'''
name: Weiqi Dong
date: 1/20/2025
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
data = pd.read_csv('data/plant_data.csv')

# 2. Histograms
# Set the style for the plots
sns.set(style="whitegrid")

# Plot histogram for leaf width
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='Leaf_Width', hue='Plant_Name', kde=True, bins=15, palette='Set1')
plt.title('Histogram of Leaf Width by Plant Type')
plt.xlabel('Leaf Width (mm)')
plt.ylabel('Frequency')
plt.show()

# Plot histogram for leaf length
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='Leaf_Length', hue='Plant_Name', kde=True, bins=15, palette='Set1')
plt.title('Histogram of Leaf Length by Plant Type')
plt.xlabel('Leaf Length (mm)')
plt.ylabel('Frequency')
plt.show()

# 3. Boxplots
# Plot boxplot for leaf width
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='Plant_Name', y='Leaf_Width', palette='Set2')
plt.title('Boxplot of Leaf Width by Plant Type')
plt.xlabel('Plant Name')
plt.ylabel('Leaf Width (mm)')
plt.show()

# Plot boxplot for leaf length
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='Plant_Name', y='Leaf_Length', palette='Set2')
plt.title('Boxplot of Leaf Length by Plant Type')
plt.xlabel('Plant Name')
plt.ylabel('Leaf Length (mm)')
plt.show()

# 4. Scatter Plot
# Plot scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Leaf_Width', y='Leaf_Length', hue='Plant_Name', palette='Set1', s=100)
plt.title('Scatter Plot of Leaf Width vs Leaf Length')
plt.xlabel('Leaf Width (mm)')
plt.ylabel('Leaf Length (mm)')
plt.legend(title='Plant Name')
plt.show()

# 5. Calculate Statistics
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
stats = data.groupby('Plant_Name').agg({
    'Leaf_Width': ['mean', 'median', 'var', 'std'],
    'Leaf_Length': ['mean', 'median', 'var', 'std']
})
print("Statistics:")
print(stats)


