import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("/Users/daneshkumar/Desktop/file_organizer/retail_cleaned.csv")

# Total revenue
total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue)

# Top 10 countries by revenue
country_sales = df.groupby('Country')['Revenue'].sum()

print("\nTop Countries:")
print(country_sales.sort_values(ascending=False).head(10))

# Top 10 products
top_products = df.groupby('Description')['Revenue'].sum()

print("\nTop Products:")
print(top_products.sort_values(ascending=False).head(10))

# Top 10 products chart
top_products.sort_values(ascending=False).head(10).plot(kind='bar')

plt.title("Top 10 Products by Revenue")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
# Top countries chart
country_sales.sort_values(ascending=False).head(10).plot(kind='bar')

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Top countries by revenue
country_sales = df.groupby('Country')['Revenue'].sum()

country_sales.sort_values(ascending=False).head(10).plot(kind='bar')

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Month-Year column
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# Monthly revenue
monthly_sales = df.groupby('Month')['Revenue'].sum()

# Plot monthly sales
monthly_sales.plot(kind='line', figsize=(10,5))

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# old charts code

plt.show()

# Monthly trend code
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Revenue'].sum()

monthly_sales.plot(kind='line', figsize=(10,5))

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
# Top customers by revenue

customer_revenue = df.groupby('Customer ID')['Revenue'].sum()

print("\nTop Customers:")
print(customer_revenue.sort_values(ascending=False).head(10))

# Customer revenue chart
customer_revenue.sort_values(ascending=False).head(10).plot(
    kind='bar',
    figsize=(10,5)
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue")

plt.tight_layout()

plt.show()
# Top customers by revenue

customer_revenue = df.groupby('Customer ID')['Revenue'].sum()

print("\nTop Customers:")
print(customer_revenue.sort_values(ascending=False).head(10))

# Customer revenue chart
customer_revenue.sort_values(ascending=False).head(10).plot(
    kind='bar',
    figsize=(10,5)
)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue")

plt.tight_layout()

plt.show()