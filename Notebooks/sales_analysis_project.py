# =========================================================
# SECTION 1 — Import Libraries
# =========================================================

import pandas as pd
import numpy as np


# =========================================================
# SECTION 2 — Load Dataset
# =========================================================

df = pd.read_csv("Downloads/Sample - Superstore.csv", encoding="latin1")
df.head()


# =========================================================
# SECTION 3 — Basic Data Inspection
# =========================================================

df.shape

df.head

df.columns

df.info

df.info()

df.dtypes


# =========================================================
# SECTION 4 — Date Conversion
# =========================================================

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])


# =========================================================
# SECTION 5 — Overall Sales & Profit
# =========================================================

df[['Sales','Profit']].sum()


# =========================================================
# SECTION 6 — Year Analysis
# =========================================================

df['Order Date'].dt.year.unique()

df['Year'] = df['Order Date'].dt.year

sales_by_year = df.groupby('Year')['Sales'].sum()

sales_by_year

profit_by_year = df.groupby('Year')['Profit'].sum()

profit_by_year


# =========================================================
# SECTION 7 — Category Analysis
# =========================================================

top_categories = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

top_categories

profit_by_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

profit_by_category


# =========================================================
# SECTION 8 — Regional Analysis
# =========================================================

sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

sales_by_region

profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

profit_by_region


# =========================================================
# SECTION 9 — Sub Category Analysis
# =========================================================

top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)

top_products

profit_by_subcategory = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)

profit_by_subcategory


# =========================================================
# SECTION 10 — Discount Analysis
# =========================================================

df[['Discount','Profit']].corr()

discount_by_category = df.groupby('Sub-Category')['Discount'].mean().sort_values(ascending=False)

discount_by_category


# =========================================================
# SECTION 11 — Loss Category Investigation
# =========================================================

loss_products = df[df['Sub-Category'].isin(['Tables','Bookcases','Supplies'])]

loss_products.groupby('Sub-Category')[['Sales','Profit','Discount']].mean()


# =========================================================
# SECTION 12 — Tables Loss by Region
# =========================================================

df[df['Sub-Category']=='Tables'].groupby('Region')['Profit'].sum()


# =========================================================
# SECTION 13 — Discount vs Profit
# =========================================================

df.groupby('Discount')['Profit'].mean().sort_index()


# =========================================================
# SECTION 14 — Loss Analysis by Region
# =========================================================

loss_products_region = df[df['Sub-Category'].isin(['Tables','Bookcases','Supplies'])]

loss_products_region.groupby(['Sub-Category','Region'])['Profit'].sum()


# =========================================================
# SECTION 15 — Supplies Summary
# =========================================================

df[df['Sub-Category']=='Supplies'][['Sales','Profit']].describe()


# =========================================================
# SECTION 16 — City Sales
# =========================================================

top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)

top_cities


# =========================================================
# SECTION 17 — City Profit
# =========================================================

top_profit_cities = df.groupby('City')['Profit'].sum().sort_values(ascending=False).head(10)

top_profit_cities


# =========================================================
# SECTION 18 — Monthly Sales
# =========================================================

df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales


# =========================================================
# SECTION 19 — Top Products
# =========================================================

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

top_products


# =========================================================
# SECTION 20 — Segment Analysis
# =========================================================

segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)

segment_sales


# =========================================================
# SECTION 21 — Business Summary
# =========================================================

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
profit_margin = total_profit / total_sales

total_sales, total_profit, total_orders, profit_margin


# =========================================================
# SECTION 22 — Monthly Time Series
# =========================================================

monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index()

monthly_sales


# =========================================================
# SECTION 23 — Dashboard Tables
# =========================================================

sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()

sales_by_category

sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()

sales_by_region

sales_by_segment = df.groupby('Segment')['Sales'].sum().reset_index()

sales_by_segment

top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()
profit_by_category = df.groupby('Category')['Profit'].sum().reset_index()

sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()

sales_by_segment = df.groupby('Segment')['Sales'].sum().reset_index()

top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index()
monthly_sales['Order Date'] = monthly_sales['Order Date'].astype(str)


# =========================================================
# SECTION 24 — Export Tables
# =========================================================

sales_by_category.to_csv('sales_by_category.csv', index=False)
profit_by_category.to_csv('profit_by_category.csv', index=False)

sales_by_region.to_csv('sales_by_region.csv', index=False)
profit_by_region.to_csv('profit_by_region.csv', index=False)

sales_by_segment.to_csv('sales_by_segment.csv', index=False)

top_cities.to_csv('top_cities.csv', index=False)
top_products.to_csv('top_products.csv', index=False)

monthly_sales.to_csv('monthly_sales.csv', index=False)


# =========================================================
# SECTION 25 — File System Checks
# =========================================================

import os
os.listdir()

import os
os.getcwd()


# =========================================================
# SECTION 26 — Orders Export
# =========================================================

total_orders = df['Order ID'].nunique()

import pandas as pd

total_orders_df = pd.DataFrame({
    'Metric': ['Total Orders'],
    'Value': [total_orders]
})

total_orders_df.to_csv('total_orders.csv', index=False)

total_orders_df


# =========================================================
# SECTION 27 — Profit by Segment
# =========================================================

profit_by_segment = df.groupby('Segment')['Profit'].sum().reset_index()

profit_by_segment


# =========================================================
# SECTION 28 — Reload Dataset
# =========================================================

import pandas as pd
import numpy as np

df = pd.read_csv("Downloads/Sample - Superstore.csv", encoding="latin1")


# =========================================================
# SECTION 29 — Loss Products Analysis
# =========================================================

loss_products = df[df['Profit'] < 0]

loss_products_summary = loss_products.groupby('Product Name')['Profit'].sum().reset_index()

loss_products_summary = loss_products_summary.sort_values(by='Profit')

loss_products_summary.head(10)


# =========================================================
# SECTION 30 — Loss Products Alternative
# =========================================================

loss_products = df.groupby('Product Name')['Profit'].sum().reset_index()

loss_products = loss_products[loss_products['Profit'] < 0]

loss_products = loss_products.sort_values(by='Profit')

loss_products


# =========================================================
# SECTION 31 — High Loss Products
# =========================================================

loss_products = df.groupby('Product Name')['Profit'].sum().reset_index()

loss_products = loss_products[loss_products['Profit'] < -100]

loss_products = loss_products.sort_values(by='Profit')

loss_products


# =========================================================
# SECTION 32 — Export Loss Products
# =========================================================

loss_products.to_csv('loss_products.csv', index=False)


# =========================================================
# SECTION 33 — Top 10 Loss Products
# =========================================================

loss_products_top10 = loss_products.head(10)

loss_products_top10.to_csv('loss_products.csv', index=False)
