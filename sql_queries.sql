-- View first 10 rows
SELECT * FROM retail_data
LIMIT 10;

-- Top countries by revenue
SELECT Country,
ROUND(SUM(REVENUE),2) AS total_revenue
FROM retail_data
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;

-- Top products by revenue
SELECT Description,
ROUND(SUM(REVENUE),2) AS total_revenue
FROM retail_data
GROUP BY Description
ORDER BY total_revenue DESC
LIMIT 10;

-- Highest priced products
SELECT Description,
MAX(price) AS highest_price
FROM retail_data
GROUP BY Description
ORDER BY highest_price DESC
LIMIT 10;

-- Top products by quantity sold
SELECT Description,
SUM(quantity) AS total_quantity
FROM retail_data
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 10;

-- Monthly revenue trend
SELECT substr(InvoiceDate,1,7) AS month,
ROUND(SUM(REVENUE),2) AS monthly_revenue
FROM retail_data
GROUP BY month
ORDER BY month;

-- Average revenue by country
SELECT Country,
ROUND(avg(REVENUE),2) AS avg_revenue
FROM retail_data
GROUP BY Country
ORDER BY avg_revenue DESC
LIMIT 10;