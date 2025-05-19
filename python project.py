# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\hp\\loan_data(Mainsheet).csv")
# Display the first few rows of the dataset     

# Clean 'Income' column: remove '?', commas, and convert to float
df['Income'] = df['Income'].str.replace("?", "", regex=False).str.replace(",", "").astype(float)

# Clean column name: remove whitespace from ' ITL '
df.rename(columns={' ITL ': 'ITL'}, inplace=True)

# Flag suspiciously high loan amounts (> 100,000 for example)
df['Suspicious'] = df['Loan_Amount'] > 100000


# %%
# Summary of suspicious transactions
print("\nSuspicious Transactions Count:")
print(df['Suspicious'].value_counts())

# %%
# Plot distribution of loan amounts
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Loan_Amount', hue='Suspicious', bins=30, kde=True, palette='coolwarm')
plt.title("Loan Amount Distribution with Suspicious Flags")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# %%
# Plot loan approval rates by employment status
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Employment_Status', hue='Approval', palette='Set2')
plt.title("Loan Approval by Employment Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# %%
# Export flagged transactions
df[df['Suspicious']].to_csv("flagged_loans.csv", index=False)
print("\nExported suspicious transactions to 'flagged_loans.csv'")

# %%


