import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Retail Performance Analysis: Inventory Turnover Optimization
# Author: 23f3002416@ds.study.iitm.ac.in
# Data Storytelling with LLMs - Created with LLM assistance
# Generated with: ChatGPT Codex (https://chatgpt.com/codex/tasks)
# LLM Tool: AI-assisted code generation for data analysis and visualization

# Define the quarterly inventory turnover data
quarterly_data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Turnover_Ratio': [3.83, 1.8, 4.77, 9.51]
}

# Create DataFrame
df = pd.DataFrame(quarterly_data)

# Calculate average (as specified in requirements)
average_turnover = 4.98  # Specified average from requirements
industry_target = 8

print(f"Inventory Turnover Analysis - Retail Performance")
print(f"=" * 50)
print(f"Author: 23f3002416@ds.study.iitm.ac.in")
print(f"Analysis Date: January 2025")
print(f"")
print(f"Quarterly Inventory Turnover Ratios:")
for i, row in df.iterrows():
    print(f"  {row['Quarter']}: {row['Turnover_Ratio']}")
print(f"")
print(f"Average Turnover Ratio: {average_turnover}")
print(f"Industry Target: {industry_target}")
print(f"Performance Gap: {industry_target - average_turnover:.2f}")

# Create simple but effective visualization
plt.figure(figsize=(10, 6))

# Plot quarterly data
plt.plot(df['Quarter'], df['Turnover_Ratio'], marker='o', linewidth=3, 
         markersize=10, color='#e74c3c', label='Actual Turnover')
plt.axhline(y=industry_target, color='#27ae60', linestyle='--', linewidth=2, 
            label=f'Industry Target ({industry_target})')
plt.axhline(y=average_turnover, color='#f39c12', linestyle=':', linewidth=2, 
            label=f'Current Average ({average_turnover})')

# Fill area under curve
plt.fill_between(df['Quarter'], 0, df['Turnover_Ratio'], alpha=0.3, color='#e74c3c')

# Styling
plt.title('Inventory Turnover Ratio Analysis\nCritical Performance Gap Requiring Immediate Action', 
          fontsize=14, fontweight='bold', pad=20)
plt.ylabel('Inventory Turnover Ratio', fontweight='bold')
plt.xlabel('Quarter', fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ylim(0, 10)

# Add annotations
plt.annotate('Crisis Point\nQ2: 1.8 (-78%)', xy=(1, 1.8), xytext=(1.5, 3),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, color='red', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.8))

plt.annotate('Recovery\nQ4: 9.51 (+19%)', xy=(3, 9.51), xytext=(2.2, 7.5),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=10, color='green', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.8))

plt.tight_layout()
plt.savefig('inventory_turnover_analysis.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"\nKey Business Insights:")
print(f"1. Q2 2024 crisis point with 1.8 turnover ratio (78% below target)")
print(f"2. Current average of {average_turnover} represents {((industry_target-average_turnover)/industry_target)*100:.1f}% performance gap")
print(f"3. Q4 recovery shows potential for improvement with proper strategy")
print(f"4. Solution focus: optimize supply chain and demand forecasting")

print(f"\nStrategic Recommendations:")
print(f"- Implement advanced demand forecasting algorithms")
print(f"- Optimize supplier lead times and ordering frequency") 
print(f"- Establish dynamic inventory rebalancing system")
print(f"- Deploy real-time inventory monitoring dashboard")

print(f"\nVisualization saved as 'inventory_turnover_analysis.png'")

# Save data for version control
df.to_csv('quarterly_turnover_data.csv', index=False)
print(f"Data saved as 'quarterly_turnover_data.csv'")