#Task 1 
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

PRICE1 = 300
PRICE2 = 200
FIXED_COST = 2_000_000
N_TRIALS = 100

C1_MEAN, C2_MEAN, C3_MEAN = 67, 85, 30
X1_MEAN, X2_MEAN = 1700, 1000
C1_SD, C2_SD, C3_SD = 5, 5, 3
X1_SD, X2_SD = 200, 150

profits = []

for i in range(N_TRIALS):
    C1 = random.gauss(C1_MEAN, C1_SD)
    C2 = random.gauss(C2_MEAN, C2_SD)
    C3 = random.gauss(C3_MEAN, C3_SD)
    X1 = random.gauss(X1_MEAN, X1_SD)
    X2 = random.gauss(X2_MEAN, X2_SD)
    profit = (PRICE1 + PRICE2 - C1 - C2 - C3) * X1 * X2 - FIXED_COST
    profits.append(profit)
    print(f"Trial {i+1:03d}: C1={C1:.2f}, C2={C2:.2f}, C3={C3:.2f}, X1={X1:.2f}, X2={X2:.2f}, Profit={profit:,.2f} $")

profits = np.array(profits)
mean_profit = np.mean(profits)
variance = np.var(profits)
std_dev = np.std(profits)
conf_low = mean_profit - 1.96 * std_dev / np.sqrt(N_TRIALS)
conf_high = mean_profit + 1.96 * std_dev / np.sqrt(N_TRIALS)
loss_prob = np.sum(profits < 0) / N_TRIALS

print("\n===== TASK 1: Monte Carlo Risk Analysis =====")
print(f"Expected Profit (Mean): {mean_profit:,.2f} $")
print(f"Variance: {variance:,.2f}")
print(f"Std Deviation: {std_dev:,.2f} $")
print(f"95% Confidence Interval: ({conf_low:,.2f} $, {conf_high:,.2f} $)")
print(f"Probability of Loss: {loss_prob*100:.2f} %")

def millions(x, pos):
    return f'${x*1e-6:.1f}M'

plt.figure(facecolor='white')
plt.hist(profits, bins=25, color='skyblue', edgecolor='black', alpha=0.8)
plt.axvline(mean_profit, color='red', linestyle='--', linewidth=2, label=f"Mean Profit: ${mean_profit:,.0f}")
plt.axvline(0, color='black', linestyle='-', linewidth=1.5, label='Break-even ($0)')
plt.title("Distribution of Simulated Profit Outcomes")
plt.xlabel("Profit ($)")
plt.ylabel("Frequency (Number of Trials)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

ax = plt.gca()
ax.xaxis.set_major_formatter(FuncFormatter(millions))
ax.xaxis.set_major_locator(MultipleLocator(100_000_000))  # فاصل 100 مليون بين الأرقام
plt.xticks(rotation=45, ha='right')  # يخليهم مائلين شوية ومرتبين

plt.tight_layout()
plt.show()
