-- Project: i used SQL to identify loss-making sub-categories and validate discount impact on profitability.

CREATE DATABASE retail_analysis;
USE retail_analysis;
DROP Database retail_analysis;

SELECT COUNT(*) 
FROM superstore;

SELECT * FROM superstore LIMIT 300;

-- 1. Category Performance :
SELECT Category,
       SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category;
-- What to say: which category earns most revenue ?     Q2.Which category gives most profit ?

-- 2. Sub-Category Loss Analysis
SELECT Sub_Category,
	   SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Sub_Category
ORDER BY Total_Profit ASC;
-- This Proves : Tables, Supplies & Bookcases are loss-making

-- 3. Discount impact
SELECT Sub_Category,
        AVG(Discount) AS Avg_Discount,
        SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Sub_Category
ORDER BY Avg_Discount DESC;
-- What you Analyze : High Discount -> LOw Profit ?

-- 4.Region Performance 
SELECT Region,
       SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region ;
-- Insight: Which region is Profitable & Which region is weak?

-- 5.Top Profitable Products
SELECT Product_Name,
	   SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Product_Name
ORDER BY Total_Profit DESC 
LIMIT 10;

-- 6.Loss Making Orders
SELECT *
FROM superstore
WHERE Profit < 0 ;
-- use this to: Analyze Patterns. Check discount / category

-- 7. customer Insights :
-- Q.7: Top 10 customers by total purchase value ?
Select Customer_Name, Customer_ID, (Round(SUM(Sales),2 )) AS Total_Spent
From superstore
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Spent DESC
LIMIT 10;

-- Q.8: How many unique customers per segment ?
Select Segment, COUNT(DISTINCT  Customer_ID) AS Unique_Customers
From superstore
GROUP BY Segment;

-- 8. Discount Impact : Does high discount lead to loss ? (Discount >20 % )
SELECT Discount, COUNT(*) AS Orders,
       ROUND(SUM(Profit),2) AS Total_Profit
FROM superstore
WHERE Discount > 0.20
GROUP BY Discount 
ORDER BY Discount DESC;

-- 9. Shipping & Operations : Average shipping delay (days) per ship Mode :
SELECT Ship_Mode,
	   ROUND(AVG(DATEDIFF(
			STR_TO_DATE(Ship_Date, '%Y-%m-%d'),
			STR_TO_DATE(Order_Date, '%Y-%m-%d'))), 0)  AS Avg_Days
FROM superstore
GROUP BY Ship_Mode
ORDER BY Avg_Days;

-- 10. Geographic Analysis : Which state has the most orders ?
SELECT State, COUNT(*) AS Total_Orders
FROM superstore
GROUP BY State
ORDER BY Total_Orders DESC
LIMIT 10;

-- city-level profit ranking:
SELECT City, State, ROUND(SUM(Profit), 2) AS City_Profit
FROM superstore
GROUP BY City, State
ORDER BY City_Profit DESC 
LIMIT 10;

-- 11. year-on-year Trend : Annual Sales trend:
SELECT YEAR(STR_TO_DATE(Order_Date, '%Y-%m-%d')) AS Year,
	    ROUND(SUM(Sales), 2) AS Annual_Sales
FROM superstore
GROUP BY Year
ORDER BY Year;

