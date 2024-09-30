import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
data1 = np.random.normal(loc=0, scale=1, size=1000)  # Normal distribution with mean 0, std 1
data2 = np.random.normal(loc=0.5, scale=1.2, size=1000)  # Normal distribution with different mean and std

# Kolmogorov-Smirnov test (Non-parametric)
ks_stat, ks_pvalue = stats.ks_2samp(data1, data2)
print(f"Kolmogorov-Smirnov test: Statistic={ks_stat}, p-value={ks_pvalue}")

# T-test (Parametric, assumes normality)
t_stat, t_pvalue = stats.ttest_ind(data1, data2)
print(f"T-test: Statistic={t_stat}, p-value={t_pvalue}")

# Mann-Whitney U test (Non-parametric)
mw_stat, mw_pvalue = stats.mannwhitneyu(data1, data2)
print(f"Mann-Whitney U test: Statistic={mw_stat}, p-value={mw_pvalue}")

# Visualize the distributions
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.legend(loc='upper right')
plt.title('Distribution Comparison')
plt.show()
