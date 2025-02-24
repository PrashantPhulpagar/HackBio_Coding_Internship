# Upload Files
from google.colab import files

# Upload both files (Manually select them when prompted)
uploaded = files.upload()

# Load the Excel files
import pandas as pd

# Load SIFT dataset
sift_df = pd.read_excel("SIFT.xlsx")

# Load FoldX dataset
foldx_df = pd.read_excel("FoldX.xlsx")

# Check the first few rows
print("\n🔹 SIFT Dataset Preview:")
print(sift_df.head())

print("\n🔹 FoldX Dataset Preview:")
print(foldx_df.head())

# Merge SIFT and FoldX datasets on 'Protein' and 'Amino_Acid'
merged_df = pd.merge(sift_df, foldx_df, on=['Protein', 'Amino_Acid'], how='inner')

# Display the first few rows of the merged dataset
print(merged_df.head())

filtered_df = merged_df[(merged_df['sift_Score'] < 0.05) & (merged_df['foldX_Score'] > 2)]
print(filtered_df)

# Extract the original amino acid (e.g., E63D → E)
merged_df["Original_AA"] = merged_df["Amino_Acid"].str[0]

# Count occurrences of each original amino acid
amino_acid_counts = merged_df["Original_AA"].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart of amino acid frequency
plt.figure(figsize=(10, 5))
sns.barplot(x=amino_acid_counts.index, y=amino_acid_counts.values, palette="viridis")
plt.xlabel("Amino Acid")
plt.ylabel("Frequency")
plt.title("Frequency of Amino Acid Mutations")
plt.show()

# Pie chart of amino acid distribution
plt.figure(figsize=(7, 7))
plt.pie(amino_acid_counts, labels=amino_acid_counts.index, autopct="%1.1f%%", colors=sns.color_palette("viridis", len(amino_acid_counts)))
plt.title("Distribution of Amino Acid Mutations")
plt.show()

# Find the most impactful amino acid
most_impactful_aa = amino_acid_counts.idxmax()
most_impactful_count = amino_acid_counts.max()

print(f"The amino acid with the highest impact on protein structure and function is {most_impactful_aa}, occurring {most_impactful_count} times.")

# Filter amino acids with more than 100 occurrences
high_freq_aa = amino_acid_counts[amino_acid_counts > 100]

print("Amino acids with more than 100 occurrences:")
print(high_freq_aa)

# Compute correlation
correlation = merged_df[['sift_Score', 'foldX_Score']].corr()

print("Correlation between SIFT and FoldX Scores:\n", correlation)

# Generate summary statistics
print("Descriptive Statistics:\n", merged_df[['sift_Score', 'foldX_Score']].describe())

#@markdown ### **Key Insights**
#@markdown - The most impacted amino acid is crucial for protein stability or function, affecting folding or interactions.
#@markdown - High-frequency mutations occur in structurally important (e.g., α-helices, β-sheets) or functionally critical (e.g., active sites, binding regions) residues.
#@markdown - Hydrophobic mutations can disrupt stability, while hydrophilic ones may alter solubility or enzymatic activity.
#@markdown - These hotspots indicate strong selective pressure and potential functional significance.