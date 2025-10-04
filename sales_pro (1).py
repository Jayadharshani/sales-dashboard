import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"c:\Users\user\OneDrive\Documents\sales.csv")
print("SALES DATA")

print(data.head())

total_revenue = data['Revenue'].sum()
total_quantity = data['Quantity'].sum()
print("\nTotal Revenue:", total_revenue)
print("Total Quantity Sold:", total_quantity)

best_product = data.groupby('Product')['Quantity'].sum().idxmax()
print("Best-selling Product:", best_product)

avg_revenue = data.groupby('Product')['Revenue'].mean()
print("\nAverage Revenue per Product:")
print(avg_revenue)

product_quantity = data.groupby('Product')['Quantity'].sum()
product_quantity.plot(kind= 'bar',color = 'blue')
plt.title("Total Quantity Sold per Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.show()

product_revenue = data.groupby('Product')['Quantity'].sum()
product_revenue.plot(kind ='pie', autopct='%1.1f%%', startangle = 90)
plt.title("Revenue Share per Product")
plt.ylabel("")
plt.show()