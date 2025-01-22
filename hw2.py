'''
Name: Weiqi Dong
Date: 1/20/2025
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
data = pd.read_csv('data/plant_data.csv')

# Define plant types and colors
plant_types = data['Plant_Name'].unique()
palette = sns.color_palette('Set2', len(plant_types))

# 2. Create Grid Layout for Leaf Width Histograms
fig, axes = plt.subplots(2, 2, figsize=(16, 14), gridspec_kw={'wspace': 0.3, 'hspace': 0.4})  # Increase figure size and spacing

# Plot All Plants in the Top-Left
sns.histplot(data=data, x='Leaf_Width', kde=True, bins=15, color='gray', ax=axes[0, 0])
axes[0, 0].set_title('All Plants')
axes[0, 0].set_xlabel('Leaf Width (mm)')
axes[0, 0].set_ylabel('Frequency')

# Plot Individual Plant Types
for i, plant in enumerate(plant_types):
    row, col = divmod(i + 1, 2)
    sns.histplot(data=data[data['Plant_Name'] == plant], x='Leaf_Width', kde=True, bins=15, color=palette[i], ax=axes[row, col])
    axes[row, col].set_title(plant)
    axes[row, col].set_xlabel('Leaf Width (mm)')
    axes[row, col].set_ylabel('Frequency')

# Add the figure title at the bottom
fig.subplots_adjust(bottom=0.1, top=0.95)  # Adjust subplot spacing
fig.text(0.5, 0.02, 'Histogram of Leaf Width', fontsize=20, weight='bold', ha='center')  # Title at the bottom
plt.show()

# 3. Create Grid Layout for Leaf Length Histograms
fig, axes = plt.subplots(2, 2, figsize=(16, 14), gridspec_kw={'wspace': 0.3, 'hspace': 0.4})  # Increase figure size and spacing

# Plot All Plants in the Top-Left
sns.histplot(data=data, x='Leaf_Length', kde=True, bins=15, color='gray', ax=axes[0, 0])
axes[0, 0].set_title('All Plants')
axes[0, 0].set_xlabel('Leaf Length (mm)')
axes[0, 0].set_ylabel('Frequency')

# Plot Individual Plant Types
for i, plant in enumerate(plant_types):
    row, col = divmod(i + 1, 2)
    sns.histplot(data=data[data['Plant_Name'] == plant], x='Leaf_Length', kde=True, bins=15, color=palette[i], ax=axes[row, col])
    axes[row, col].set_title(plant)
    axes[row, col].set_xlabel('Leaf Length (mm)')
    axes[row, col].set_ylabel('Frequency')

# Add the figure title at the bottom
fig.subplots_adjust(bottom=0.1, top=0.95)  # Adjust subplot spacing
fig.text(0.5, 0.02, 'Histogram of Leaf Length', fontsize=20, weight='bold', ha='center')  # Title at the bottom
plt.show()

# 4. Boxplots
# 4.1 Add an 'All' Column
data['All'] = 'All'  # Add an 'All' column for boxplots

# 4.2 Combine 'All' and 'Plant_Name' Data
combined_data = pd.concat([
    data[['All', 'Leaf_Width', 'Leaf_Length']].rename(columns={'All': 'Category'}),
    data[['Plant_Name', 'Leaf_Width', 'Leaf_Length']].rename(columns={'Plant_Name': 'Category'})
])

# 4.3 Define Categories and Colors
categories = ['All', 'Maple', 'Pothos', 'Rose']
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon']

# 4.4 Boxplot for Leaf Width
plt.figure(figsize=(10, 6))
box_data = [combined_data[combined_data['Category'] == cat]['Leaf_Width'] for cat in categories]
box_plot = plt.boxplot(box_data, labels=categories, patch_artist=True)  # Enable color filling

# Assign colors to each box
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Box Plot of Leaf Width (All and by Plant Type)')
plt.xlabel('Category')
plt.ylabel('Leaf Width (mm)')
plt.show()

# 4.5 Boxplot for Leaf Length
plt.figure(figsize=(10, 6))
box_data = [combined_data[combined_data['Category'] == cat]['Leaf_Length'] for cat in categories]
box_plot = plt.boxplot(box_data, labels=categories, patch_artist=True)  # Enable color filling

# Assign colors to each box
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Box Plot of Leaf Length (All and by Plant Type)')
plt.xlabel('Category')
plt.ylabel('Leaf Length (mm)')
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Leaf_Width', y='Leaf_Length', hue='Plant_Name', palette='Set1', s=100)
plt.title('Scatter Plot of Leaf Width vs Leaf Length')
plt.xlabel('Leaf Width (mm)')
plt.ylabel('Leaf Length (mm)')
plt.legend(title='Plant Name')
plt.show()

# 6. Calculate Statistics
# 6.1 Calculate statistics for each plant type
plant_stats = data.groupby('Plant_Name').agg({
    'Leaf_Width': ['mean', 'median', 'var', 'std'],
    'Leaf_Length': ['mean', 'median', 'var', 'std']
}).stack().reset_index()

# 6.2 Calculate statistics for all plants combined
all_stats = pd.DataFrame({
    'Category': ['All', 'All', 'All', 'All'],
    'Statistic': ['mean', 'median', 'var', 'std'],
    'Leaf_Width': [
        data['Leaf_Width'].mean(),
        data['Leaf_Width'].median(),
        data['Leaf_Width'].var(),
        data['Leaf_Width'].std()
    ],
    'Leaf_Length': [
        data['Leaf_Length'].mean(),
        data['Leaf_Length'].median(),
        data['Leaf_Length'].var(),
        data['Leaf_Length'].std()
    ]
})

# 6.3 Rename columns for consistency
plant_stats = plant_stats.rename(columns={'level_1': 'Statistic', 'Plant_Name': 'Category'})

# 6.4 Combine plant-specific and overall statistics
combined_stats = pd.concat([all_stats, plant_stats], ignore_index=True)

# 6.5 Print statistics
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print("Statistics:")
print(combined_stats)