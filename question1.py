# question1.py

from installation import load_and_prepare_data
import matplotlib.pyplot as plt
import seaborn as sns

df = load_and_prepare_data()

# --- Question 1: What is the most frequent inquiry type? ---
inquiry_counts = df['inquiry_type'].value_counts()

colors = ['tomato' if x == 'Product Defect' else 'lightgray' for x in inquiry_counts.index]

# Visualize with bar graph
plt.figure(figsize=(10, 6))
sns.barplot(x=inquiry_counts.index, y=inquiry_counts.values, palette=colors)

plt.title('Most Frequent Inquiry Types (Highlighting Core Problem)', fontsize=16)
plt.ylabel('Number of Inquiries')
plt.xlabel('Inquiry Type')
plt.show()
