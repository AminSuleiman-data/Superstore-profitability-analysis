# =========================================================
# 1. Import Libraries
# =========================================================

import pandas as pd
import numpy as np


# =========================================================
# 2. Check Working Directory
# =========================================================

import os
os.getcwd()


# =========================================================
# 3. Load Dataset
# =========================================================

df=pd.read_csv("Sample - Superstore.csv", encoding="latin1")
df.head()


# =========================================================
# 4. Dataset Overview
# =========================================================

df.shape

df.columns

df.info()


# =========================================================
# 5. Data Types
# =========================================================

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df.dtypes


# =========================================================
# 6. Overall Sales & Profit
# =========================================================

df[['Sales','Profit']].sum()


# =========================================================
# 7. Extract Year from Order Date
# =========================================================

df['Order Date'].dt.year.unique()

df['Year'] = df['Order Date'].dt.year


# =========================================================
# 8. Sales & Profit by Year
# =========================================================

sales_by_year = df.groupby('Year')['Sales'].sum()
sales_by_year

profit_by_year = df.groupby('Year')['Profit'].sum()
profit_by_year


# =========================================================
# 9. Sales by Category
# =========================================================

Sales_by_Categories = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
Sales_by_Categories


# =========================================================
# 10. Profit by Category
# =========================================================

Profit_by_Categories = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
Profit_by_Categories


# =========================================================
# 11. Sales by Region
# =========================================================

sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

sales_by_region


# =========================================================
# 12. Profit by Region
# =========================================================

profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

profit_by_region


# =========================================================
# 13. Sales by Sub-Category
# =========================================================

Sales_by_subcategory = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)

Sales_by_subcategory


# =========================================================
# 14. Profit by Sub-Category
# =========================================================

profit_by_subcategory = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)

profit_by_subcategory


# =========================================================
# 15. Discount vs Profit Correlation
# =========================================================

df[['Discount','Profit']].corr()


# =========================================================
# 16. Average Discount by Sub-Category
# =========================================================

discount_by_Subcategory = df.groupby('Sub-Category')['Discount'].mean().sort_values(ascending=False)

discount_by_Subcategory


# =========================================================
# 17. Loss Sub-Categories Analysis
# =========================================================

loss_subcategorys = df[df['Sub-Category'].isin(['Supplies','Bookcases','Tables'])]
loss_subcategorys.groupby('Sub-Category')[['Sales','Profit','Discount']].mean()


# =========================================================
# 18. Tables Profit by Region
# =========================================================

df[df['Sub-Category']=='Tables'].groupby('Region')['Profit'].sum()


# =========================================================
# 19. Profit by Discount
# =========================================================

df.groupby('Discount')['Profit'].sum()


# =========================================================
# 20. Discount Distribution
# =========================================================

df.groupby('Discount').size().sort_index()


# =========================================================
# 21. Loss Sub-Categories by Region
# =========================================================

loss_Subcategorys_by_region = df[df['Sub-Category'].isin(['Tables','Bookcases','Supplies'])]

loss_Subcategorys_by_region.groupby(['Sub-Category','Region'])['Profit'].sum()


# =========================================================
# 22. Deep Dive — Supplies
# =========================================================

df[df['Sub-Category']=='Supplies'][['Sales','Profit']].describe()

df[df['Sub-Category']=='Supplies'].sort_values('Profit').head(10)

df[(df['Sub-Category']=='Supplies') & (df['Profit'] < 0)].shape

df[df['Sub-Category']=='Supplies'].groupby(df['Profit'] < 0)['Sales'].mean()

df[df['Sub-Category']=='Supplies']['Profit'].sum()

df[df['Sub-Category']=='Supplies'].nsmallest(10,'Profit')[['Sales','Profit']]


# =========================================================
# 23. Deep Dive — Bookcases
# =========================================================

df[df['Sub-Category']=='Bookcases'][['Sales','Profit']].describe()

df[df['Sub-Category']=='Bookcases'].sort_values('Profit').head(10)

df[(df['Sub-Category']=='Bookcases') & (df['Profit'] < 0)].shape

df[df['Sub-Category']=='Bookcases'].groupby(df['Profit'] < 0)['Sales'].mean()

df[df['Sub-Category']=='Bookcases']['Profit'].sum()


# =========================================================
# 24. Deep Dive — Tables
# =========================================================

df[df['Sub-Category']=='Tables'][['Sales','Profit']].describe()

df[df['Sub-Category']=='Tables'].sort_values('Profit').head(10)

df[(df['Sub-Category']=='Tables') & (df['Profit'] < 0)].shape

df[df['Sub-Category']=='Tables'].groupby(df['Profit'] < 0)['Sales'].mean()

df[df['Sub-Category']=='Tables']['Profit'].sum()


# =========================================================
# 25. Top Cities Analysis
# =========================================================

Top_cities_by_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)

Top_cities_by_sales

Top_cities_by_Profit = df.groupby('City')['Profit'].sum().sort_values(ascending=False).head(10)
Top_cities_by_Profit


# =========================================================
# 26. Monthly Sales
# =========================================================

df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales


# =========================================================
# 27. Top Products by Sales
# =========================================================

top_products_by_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

top_products_by_sales


# =========================================================
# 28. Overall Business Metrics
# =========================================================

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
total_sales, total_profit, total_orders


# =========================================================
# 29. Sales by Segment
# =========================================================

Sales_by_segment = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

Sales_by_segment


# =========================================================
# 30. Profit by Segment
# =========================================================

profit_by_segment = df.groupby('Segment')['Profit'].sum().sort_values(ascending=False)

profit_by_segment


# =========================================================
# 31. Category Analysis (Second Version)
# =========================================================

sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

sales_by_category

Profit_by_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
Profit_by_category


# =========================================================
# 32. Region Analysis (Second Version)
# =========================================================

sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

sales_by_region

Profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

Profit_by_region


# =========================================================
# 33. Loss Products
# =========================================================

loss_products = df.groupby('Product Name')['Profit'].sum().reset_index()

loss_products = loss_products[loss_products['Profit'] < 0]

loss_products = loss_products.sort_values(by='Profit')

loss_products


# =========================================================
# 34. Top Loss Products
# =========================================================

top_loss_making_products = df.groupby('Product Name')['Profit'].sum().reset_index()

top_loss_making_products = loss_products[loss_products['Profit'] < -100]

top_loss_making_products = loss_products.sort_values(by='Profit')

top_loss_making_products


# =========================================================
# 35. Export Analysis Results
# =========================================================

# Sales and Profit by Category
sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

# Sales and Profit by Region
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()

# Sales and Profit by Segment
sales_by_segment = df.groupby('Segment')['Sales'].sum().reset_index()
profit_by_segment = df.groupby('Segment')['Profit'].sum().reset_index()

# Top Cities by Sales
top_cities_by_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

# Top Products by Sales
top_products_by_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

# Monthly Sales
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# Top Loss Products
loss_products_top10 = loss_products.head(10)

sales_by_category.to_csv('sales_by_category.csv', index=False)
profit_by_category.to_csv('profit_by_category.csv', index=False)

sales_by_region.to_csv('sales_by_region.csv', index=False)
profit_by_region.to_csv('profit_by_region.csv', index=False)

sales_by_segment.to_csv('sales_by_segment.csv', index=False)
profit_by_segment.to_csv('profit_by_segment.csv', index=False)

top_cities_by_sales.to_csv('top_cities_by_sales.csv', index=False)
top_products_by_sales.to_csv('top_products_by_sales.csv', index=False)

monthly_sales.to_csv('monthly_sales.csv', index=False)

loss_products_top10.to_csv('loss_products_top10.csv', index=False)


# =========================================================
# 36. Check File Export Location
# =========================================================

import os
print(os.getcwd())
