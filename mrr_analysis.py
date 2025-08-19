# mrr_analysis.py
# Author: Data Analyst using Jules (ChatGPT Codex)
# Email : 24f2007963@ds.study.iitm.ac.in

import matplotlib.pyplot as plt
import pandas as pd

# Quarterly MRR Growth Data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR_Growth": [2.06, 7.48, 12.54, 7.38]
}

df = pd.DataFrame(data)

# Average MRR Growth
avg_mrr_growth = df["MRR_Growth"].mean()
print(f"Average MRR Growth: {avg_mrr_growth:.2f}")  # Should match 7.36

# Industry benchmark
industry_target = 15

# Visualization
plt.figure(figsize=(8,5))
plt.plot(df["Quarter"], df["MRR_Growth"], marker='o', label='Company MRR Growth')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (15)')
plt.title("Quarterly MRR Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.ylim(0, max(industry_target + 5, df["MRR_Growth"].max() + 5))
plt.grid(True)
plt.legend()
plt.savefig("mrr_growth_trend.png")
plt.show()
