import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/Retail_Profit_Leakage_/02_Cleaned_Data/Sample_Superstore_final.csv")
print(df.head(6))

print(df.shape)
print(df.info())
print(df.describe(include="all"))
print(df.isnull().sum())
print()

print(f'data have {df.duplicated().sum()} dupicates value')
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("-", "_") # for subcategory column
df['Order_Date'] = pd.to_datetime(df['Order_Date']) # if order_date are not datetime fix them:
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])
print(df.columns)
print(df.shape)

print(df[['Sales','Quantity','Discount','Profit']].describe())
print(df[df['Profit'] < 0])
df['Order_Year'] = df['Order_Date'].dt.year # type: ignore
df['Order_Month'] = df['Order_Date'].dt.month # type: ignore
df['Month_Name'] = df['Order_Date'].dt.month_name() # type: ignore
# print(df.to_csv("superstore_cleaned.scv",index = False))
print(df.dtypes)

# step 1--) connect to mysql
# replace placeholder with actual details
from sqlalchemy import create_engine  

Username = 'root'
Password = 'Akash%402006'
Host=  'localhost'
Port = '3306'
database = 'retail_analysis'

engine = create_engine(f'mysql+mysqlconnector://{Username}:{Password}@{Host}:{Port}/{database}')

# step 2--> load dataframe into mysql
table_name = 'superstore'  # choose any table name
df.to_sql(table_name, engine, if_exists='replace', index= False)

print(f"Data Successfully loaded into Table '{table_name}' in Database '{database}'.")
# pd.read_sql("select * from superstore limit 20", engine)   # you can also use this , another shortcuts


#                                           PHASE-2: EDA 
# 1. Sales Overview
print(df['Sales'].sum()) # Total Revenue
print(df['Profit'].sum()) # Total Profit
# if profit is low compared to sales -> Problem exists(leakage) 


# 2. Sales by Category.
# Insight: Which category earns most revenue ?
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))
print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))
# If a category has high sales but low/negative profit -> that's your project highlight.


# 3. Sales by Region.
# Insight : Which Region is loss-Making?
# Insight: Which Region is Profitable ?
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))
print(df.groupby('Region')['Profit'].sum().sort_values(ascending=False))


# 4. Top 10 loss making Products ?
print(df.groupby('Product_Name')['Profit'].sum().sort_values().head(10)) 
# " I identify top loss-making products contributing to profit leakage."


# 5. Discount Vs Profit.
print(df[['Discount', 'Profit']].corr())
# if correlation is negative: More Discount -> less Profit
# now visualize:
plt.scatter(df['Discount'], df['Profit'])
plt.xlabel("Discount")
plt.ylabel('Profit')
plt.show()


# 6. Monthly Sales Trend .
print(df.groupby('Month_Name')['Sales'].sum())  
print(df.groupby(['Order_Year', 'Order_Month'])['Sales'].sum())
# shows : seasonal trends , Peak months


# 7. Segment Analysis.
print(df.groupby('Segment')['Profit'].sum())
# Ex: Consumer Vs Corporate Vs Home Office   ->    Which customers bring profit


# 8. Sub-Category Deep Analysis.
print(df.groupby('Sub_Category')['Profit'].sum().sort_values())
# This reveals: Exact weak areas(like: Tables, Bookcases, etc.)


# 9. Top Profitable Sub-Category
print(df.groupby('Sub_Category')['Profit'].sum().sort_values(ascending=False).head(5))
# insight: Which products are actually making money.


# 10. Sales Vs Profit Comparision.
print(df.groupby('Category')[['Sales', 'Profit']].sum())
# this shows: High_Sales {Doesn't Means} High Profit





 