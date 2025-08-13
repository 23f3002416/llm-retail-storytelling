import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Retail Performance Analysis: Inventory Turnover Optimization
# Author: 23f3002416@ds.study.iitm.ac.in
# Data Storytelling with LLMs - Created with LLM assistance for strategic analysis

# Define the quarterly inventory turnover data
quarterly_data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Turnover_Ratio': [3.83, 1.8, 4.77, 9.51],
    'Industry_Target': [8, 8, 8, 8],
    'Days': [90, 90, 90, 90]
}

# Create DataFrame
df = pd.DataFrame(quarterly_data)

# Calculate average (as specified in requirements)
average_turnover = 4.98  # Specified average from requirements
current_average = df['Turnover_Ratio'].mean()

print(f"Inventory Turnover Analysis - Retail Performance")
print(f"=" * 50)
print(f"Author: 23f3002416@ds.study.iitm.ac.in")
print(f"Analysis Date: January 2025")
print(f"")
print(f"Quarterly Inventory Turnover Ratios:")
for i, row in df.iterrows():
    print(f"  {row['Quarter']}: {row['Turnover_Ratio']}")
print(f"")
print(f"Calculated Average: {current_average:.2f}")
print(f"Required Average: {average_turnover}")
print(f"Industry Target: 8.0")
print(f"Performance Gap: {8 - average_turnover:.2f}")

# Create comprehensive visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Retail Performance Analysis: Inventory Turnover Crisis\nStrategic Data Story for Executive Decision Making', 
             fontsize=16, fontweight='bold', y=0.98)

# 1. Quarterly Trend Analysis
ax1.plot(df['Quarter'], df['Turnover_Ratio'], marker='o', linewidth=3, markersize=8, 
         color='#e74c3c', label='Actual Turnover')
ax1.axhline(y=8, color='#27ae60', linestyle='--', linewidth=2, label='Industry Target (8.0)')
ax1.axhline(y=average_turnover, color='#f39c12', linestyle=':', linewidth=2, 
            label=f'Current Average ({average_turnover})')
ax1.fill_between(df['Quarter'], 0, df['Turnover_Ratio'], alpha=0.3, color='#e74c3c')
ax1.set_title('Quarterly Inventory Turnover Trend\nCritical Performance Gap Identified', fontweight='bold')
ax1.set_ylabel('Turnover Ratio', fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 10)

# Add annotations for critical points
ax1.annotate('Crisis Point\nQ2: 1.8', xy=(1, 1.8), xytext=(1.5, 3),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, color='red', fontweight='bold')
ax1.annotate('Recovery\nQ4: 9.51', xy=(3, 9.51), xytext=(2.5, 8.5),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=10, color='green', fontweight='bold')

# 2. Performance vs Target Analysis
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
performance_gap = [8 - x for x in df['Turnover_Ratio']]
colors = ['#e74c3c' if gap > 0 else '#27ae60' for gap in performance_gap]

bars = ax2.bar(quarters, performance_gap, color=colors, alpha=0.7, edgecolor='black')
ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax2.set_title('Performance Gap Analysis\nDistance from Industry Target (8.0)', fontweight='bold')
ax2.set_ylabel('Gap from Target', fontweight='bold')
ax2.grid(True, alpha=0.3)

# Add value labels on bars
for bar, gap in zip(bars, performance_gap):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + (0.1 if height > 0 else -0.3),
             f'{gap:.2f}', ha='center', va='bottom' if height > 0 else 'top', 
             fontweight='bold')

# 3. Cost Impact Analysis (estimated)
storage_costs = [gap * 1000000 for gap in performance_gap if gap > 0]  # $1M per gap point
quarters_with_excess = [q for q, gap in zip(quarters, performance_gap) if gap > 0]

if quarters_with_excess:
    ax3.bar(quarters_with_excess, storage_costs, color='#e74c3c', alpha=0.7)
    ax3.set_title('Estimated Excess Storage Costs\nFinancial Impact of Poor Turnover', fontweight='bold')
    ax3.set_ylabel('Excess Cost ($M)', fontweight='bold')
    total_excess_cost = sum(storage_costs)
    ax3.text(0.5, max(storage_costs) * 0.8, f'Total Excess Cost:\n${total_excess_cost:.1f}M', 
             transform=ax3.transAxes, ha='center', va='center',
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8),
             fontsize=12, fontweight='bold')

# 4. Solution Roadmap
solution_months = np.arange(1, 13)
current_projection = [average_turnover + (8 - average_turnover) * (1 - np.exp(-0.3 * x)) 
                     for x in solution_months]

ax4.plot(solution_months, current_projection, color='#3498db', linewidth=3, 
         label='Projected Improvement')
ax4.axhline(y=8, color='#27ae60', linestyle='--', linewidth=2, label='Target (8.0)')
ax4.axhline(y=average_turnover, color='#e74c3c', linestyle=':', linewidth=2, 
            label=f'Current ({average_turnover})')
ax4.fill_between(solution_months, average_turnover, current_projection, 
                alpha=0.3, color='#3498db')
ax4.set_title('Solution Roadmap: 12-Month Improvement Plan\nOptimize Supply Chain & Demand Forecasting', 
              fontweight='bold')
ax4.set_xlabel('Months from Implementation', fontweight='bold')
ax4.set_ylabel('Projected Turnover Ratio', fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_ylim(4, 9)

plt.subplots_adjust(top=0.93, hspace=0.3, wspace=0.3)
plt.savefig('inventory_turnover_analysis.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"\nKey Business Insights:")
print(f"1. Q2 2024 crisis point with 1.8 turnover ratio (78% below target)")
print(f"2. Current average of {average_turnover} represents {((8-average_turnover)/8)*100:.1f}% performance gap")
print(f"3. Estimated excess storage costs exceed $12M annually")
print(f"4. Solution focus: optimize supply chain and demand forecasting")
print(f"5. Projected 12-month recovery to target performance")

print(f"\nRecommended Actions:")
print(f"- Implement advanced demand forecasting algorithms")
print(f"- Optimize supplier lead times and ordering frequency")
print(f"- Establish dynamic inventory rebalancing system")
print(f"- Deploy real-time inventory monitoring dashboard")
print(f"- Create cross-functional supply chain optimization team")

print(f"\nVisualization saved as 'inventory_turnover_analysis.png'")

# Save data for version control
df.to_csv('quarterly_turnover_data.csv', index=False)
print(f"Data saved as 'quarterly_turnover_data.csv'")