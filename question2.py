# question2.py

from installation import load_and_prepare_data
import matplotlib.pyplot as plt
import seaborn as sns

df = load_and_prepare_data()

# --- Question 2: Where do 'Product Defect' inquiries primarily come from? ---
print("\n--- Question 2: Root Cause Analysis for 'Product Defect' Inquiries ---")

df_defects = df[df['inquiry_type'] == 'Product Defect']

product_defect_counts = df_defects['product_category'].value_counts()

print("\nDistribution of 'Product Defect' inquiries by Product Category:")
print(product_defect_counts)


# Visualize the results with a pie chart
plt.figure(figsize=(10, 8))

# Set colors and explode effect to highlight the main cause ('Refrigerator')
colors = ['tomato', 'lightgray', 'whitesmoke']
explode = (0.1, 0, 0)

plt.pie(product_defect_counts, 
        labels=product_defect_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors, 
        explode=explode,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2})

plt.title("Proportion of 'Product Defect' Inquiries by Product Category", fontsize=18, pad=20)
plt.ylabel('')
plt.show()
