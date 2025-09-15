# question3.py

from installation import load_and_prepare_data
import matplotlib.pyplot as plt
import seaborn as sns

df = load_and_prepare_data()

# --- Question 3: Which issue consumes the most company time (cost)? ---
print("\n--- Question 3: Business Impact Analysis by Inquiry Type ---")

impact_analysis = df.groupby('inquiry_type')['processing_time_hours'].sum().sort_values(ascending=False)

print("\nTotal Processing Time by Inquiry Type (Consumed Resources):")
print(impact_analysis)

# Visualize the results.
plt.figure(figsize=(10, 6))
sns.barplot(x=impact_analysis.index, y=impact_analysis.values, palette='Reds_r')
plt.title('Total Hours Spent by Inquiry Type (Business Impact)', fontsize=16)
plt.ylabel('Total Processing Time (Hours)')
plt.xlabel('Inquiry Type')
plt.show()
