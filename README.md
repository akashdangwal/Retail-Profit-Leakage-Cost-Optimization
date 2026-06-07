# Retail-Profit-Leakage-Cost-Optimization Analysis
An end-to-end retail analytics project using Python, MySQL, and Power BI to identify profit leakage, analyze discount impact, and optimize business performance.

## Overview

This project investigates why a retail business was experiencing low profitability despite generating strong sales. Using Python, MySQL, and Power BI, the analysis identified key sources of profit leakage, high-loss product categories, and discounting patterns that negatively impacted overall business performance.

The goal was to provide data-driven recommendations to improve profitability and support better business decisions.

## Business Problem

Although the company generated significant sales revenue, profit margins remained low and several product categories consistently produced losses.

This project aimed to answer:

* Which products are causing the largest losses?
* How do discounts affect profitability?
* Which regions and customer segments perform best?
* Where can costs be optimized to improve profit?

## Dataset

* Retail sales dataset containing **9,994 customer orders**
* Includes sales, profit, discount, shipping, product, customer, and regional information

## Tools & Technologies

* **Python** (Pandas, NumPy, Matplotlib, Seaborn)
* **MySQL**
* **SQLAlchemy**
* **Power BI**
* **Jupyter Notebook**
* **Git & GitHub**

## Project Workflow

### 1. Data Cleaning & Preparation

* Loaded and explored the dataset using Python.
* Handled missing values and data quality issues.
* Standardized data formats for analysis.
* Exported cleaned data to MySQL using SQLAlchemy.

### 2. Exploratory Data Analysis (EDA)

* Analyzed sales, profit, discounts, and customer behavior.
* Identified trends and patterns affecting profitability.
* Examined category and sub-category performance.

### 3. SQL Analysis

Used MySQL queries to:

* Analyze regional performance.
* Identify high-value customers.
* Measure shipping delays.
* Compare sales and profit across segments.
* Investigate discount impact on profitability.

### 4. Dashboard Development

Built an interactive Power BI dashboard to monitor:

* Sales vs Profit performance
* Profit leakage areas
* Discount impact analysis
* Regional performance
* Customer segment analysis
* Product and sub-category profitability

## Key Findings

### Major Profit Leakage Sources

Three sub-categories generated the majority of losses:

* Tables
* Bookcases
* Supplies

### Discount Impact

Orders with discounts above **20%** showed a significant decline in profitability and contributed heavily to losses.

### Regional Insights

Certain regions generated strong sales but underperformed in profit due to aggressive discounting and product mix.

### Customer Insights

A small group of customers contributed a large share of revenue, highlighting opportunities for targeted retention strategies.

## Results & Recommendations

* Reduce excessive discounting, especially above 20%.
* Reevaluate pricing and inventory strategies for Tables, Bookcases, and Supplies.
* Focus on high-profit customer segments and regions.
* Monitor profit leakage through dashboard-driven decision making.

## Dashboard Highlights

* Profit Leakage Analysis
* Sales & Profit Overview
* Regional Performance Tracking
* Customer Segment Insights
* Discount vs Profit Analysis
* Interactive KPIs and Filters

## How to Run

### Python Analysis

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy pymysql
```

Run the Jupyter Notebook or Python scripts to perform data cleaning and analysis.

### MySQL

1. Create a database.
2. Import cleaned data into MySQL.
3. Execute SQL queries available in the project.

### Power BI

1. Open the `.pbix` file.
2. Refresh the data source if required.
3. Explore dashboard insights using filters and visualizations.

## Project Outcome

This project demonstrates end-to-end data analytics skills, including data cleaning, exploratory data analysis, SQL querying, business problem solving, and dashboard development. The analysis uncovered key profit leakage drivers and provided actionable recommendations to improve profitability.
