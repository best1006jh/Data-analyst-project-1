# question4.py

from installation import load_and_prepare_data
import matplotlib.pyplot as plt

df = load_and_prepare_data()

# --- Question 4: How is agent performance? (Average Resolution Time & Satisfaction) ---
print("\n--- Question 2: Agent Performance Analysis ---")

agent_performance = df.groupby('agent_name').agg(
    avg_processing_time=('processing_time_hours', 'mean'),
    avg_satisfaction_score=('satisfaction_score', 'mean')
).sort_values(by='avg_satisfaction_score', ascending=False)

print(agent_performance)

# Visualization
fig, ax1 = plt.subplots(figsize=(12, 7))

# Customer Satisfaction by Agent
ax1.set_title('Average Resolution Time & Customer Satisfaction by Agent', fontsize=16)
ax1.set_ylabel('Average Satisfaction Score', color='royalblue')
ax1.bar(agent_performance.index, agent_performance['avg_satisfaction_score'], color='royalblue', alpha=0.7, label='Satisfaction Score')
ax1.tick_params(axis='y', labelcolor='royalblue')
ax1.legend(loc='upper left')

# Average Resolution Time 
ax2 = ax1.twinx()
ax2.set_ylabel('Average Resolution Time (Hours)', color='tomato')
ax2.plot(agent_performance.index, agent_performance['avg_processing_time'], color='tomato', marker='o', linestyle='--', label='Resolution Time (Hours)')
ax2.tick_params(axis='y', labelcolor='tomato')
ax2.legend(loc='upper right')

fig.tight_layout() 
plt.show()
