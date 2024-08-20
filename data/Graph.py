import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'C:/Users/furka/team_project/data/mortgage.csv'
data = pd.read_csv(file_path)

# 1. Loan Amount vs Interest Rate (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='loan_amount', y='interest_rate', data=data)
plt.title('Loan Amount vs Interest Rate')
plt.xlabel('Loan Amount')
plt.ylabel('Interest Rate (%)')
plt.grid(True)
plt.show()

# 2. Income vs DTI (Debt-to-Income Ratio) (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='annual_inc', y='dti', data=data)
plt.title('Income vs Debt-to-Income Ratio')
plt.xlabel('Annual Income')
plt.ylabel('DTI (%)')
plt.grid(True)
plt.show()

# 3. Grade vs Interest Rate (Box Plot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='grade', y='interest_rate', data=data)
plt.title('Grade vs Interest Rate')
plt.xlabel('Grade')
plt.ylabel('Interest Rate (%)')
plt.grid(True)
plt.show()

# 4. Loan Condition vs Total Payment (Bar Plot)
loan_condition_payment = data.groupby('loan_condition')['total_pymnt'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='loan_condition', y='total_pymnt', data=loan_condition_payment)
plt.title('Loan Condition vs Average Total Payment')
plt.xlabel('Loan Condition')
plt.ylabel('Average Total Payment')
plt.grid(True)
plt.show()

# 5. Histogram of Interest Rates
plt.figure(figsize=(10, 6))
sns.histplot(data['interest_rate'], bins=30, kde=True)
plt.title('Histogram of Interest Rates')
plt.xlabel('Interest Rate (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
