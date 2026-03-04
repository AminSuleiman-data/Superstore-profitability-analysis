# =========================================================
# Superstore Sales Analysis
# Author: Amin Suleiman
# Project: Profit Margin Optimization & Discount Strategy Analysis
# =========================================================


# =========================================================
# 1. Import Libraries
# Purpose: Load required Python libraries
# =========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# visualization style
sns.set(style="whitegrid")

# =========================================================
# 2. Load Dataset
# Purpose: Import dataset into pandas dataframe
# =========================================================

df = pd.read_csv("superstore.csv")

# preview data
df.head()

# =========================================================
# 3. Basic Dataset Inspection
# Purpose: Understand dataset structure
# =========================================================

print("Dataset Shape:", df.shape)

df.info()

df.describe()

# =========================================================
# 4. Missing Values Check
# Purpose: Identify missing data
# =========================================================

missing_values = df.isnull().sum()

print("Missing Values:")
print(missing_values)

# =========================================================
# 5. Data Type Conversion
# Purpose: Ensure proper date formats
# =========================================================

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# =========================================================
# 6. Feature Engineering
# Purpose: Create additional useful columns
# =========================================================

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Profit Margin'] = df['Profit'] / df['Sales']

# =========================================================
# 7. Overall Business Performance
# Purpose: Calculate total revenue and profit
# =========================================================

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# =========================================================
# 8. Monthly Sales Trend
# Purpose: Identify seasonality patterns
# =========================================================

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# =========================================================
# 9. Regional Performance Analysis
# Purpose: Compare revenue and profit by region
# =========================================================

region_performance = df.groupby('Region')[['Sales','Profit']].sum()

print(region_performance)

region_performance.plot(kind='bar', figsize=(10,6))
plt.title("Regional Sales and Profit")
plt.show()

# =========================================================
# 10. Category Profitability Analysis
# Purpose: Evaluate profit contribution by category
# =========================================================

category_analysis = df.groupby('Category')[['Sales','Profit']].sum()

print(category_analysis)

category_analysis.plot(kind='bar', figsize=(10,6))
plt.title("Category Performance")
plt.show()

# =========================================================
# 11. Sub-Category Analysis
# Purpose: Identify strong and weak product groups
# =========================================================

sub_category_analysis = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Profit')

print(sub_category_analysis)

# =========================================================
# 12. Discount Impact Analysis
# Purpose: Understand how discounts affect profitability
# =========================================================

discount_analysis = df.groupby('Discount')['Profit'].mean()

print(discount_analysis)

# =========================================================
# 13. Correlation Analysis
# Purpose: Identify statistical relationships
# =========================================================

correlation_matrix = df[['Sales','Profit','Discount','Quantity']].corr()

print(correlation_matrix)

plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# =========================================================
# 14. Discount vs Profit Relationship
# Purpose: Visualize negative relationship
# =========================================================

plt.figure(figsize=(8,6))
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title("Discount vs Profit")
plt.show()

# =========================================================
# 15. Product Level Profitability
# Purpose: Detect high revenue but low profit products
# =========================================================

product_analysis = df.groupby('Product Name')[['Sales','Profit','Discount']].mean()

loss_products = product_analysis.sort_values(by='Profit').head(10)

print(loss_products)

# =========================================================
# 16. Customer Segment Analysis
# Purpose: Evaluate contribution by customer segments
# =========================================================

segment_analysis = df.groupby('Segment')[['Sales','Profit']].sum()

print(segment_analysis)

segment_analysis.plot(kind='bar', figsize=(10,6))
plt.title("Customer Segment Performance")
plt.show()

# =========================================================
# 17. City Level Sales Analysis
# Purpose: Identify top performing cities
# =========================================================

city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)

print(city_sales.head(10))

# =========================================================
# 18. High Discount Loss Detection
# Purpose: Detect orders where discount > 30% causing losses
# =========================================================

high_discount_losses = df[(df['Discount'] >= 0.30) & (df['Profit'] < 0)]

print(high_discount_losses[['Product Name','Sales','Discount','Profit']].head())

# =========================================================
# 19. Profit Margin Distribution
# Purpose: Understand margin distribution across orders
# =========================================================

plt.figure(figsize=(8,6))
sns.histplot(df['Profit Margin'], bins=30)
plt.title("Profit Margin Distribution")
plt.show()

# =========================================================
# END OF ANALYSIS
# =========================================================
