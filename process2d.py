import pandas as pd
import numpy as np

# 加载数据
data_path = "pls_sem_data.csv"
data = pd.read_csv(data_path)

# 信度分析: Cronbach's Alpha 计算
def cronbach_alpha(items_scores):
    """Calculate Cronbach's Alpha for given items."""
    item_variances = items_scores.var(axis=0, ddof=1)
    total_score_variance = items_scores.sum(axis=1).var(ddof=1)
    n_items = items_scores.shape[1]
    return (n_items / (n_items - 1)) * (1 - sum(item_variances) / total_score_variance)

# 定义构念及其对应变量
constructs = {
    "教育性体验": ["EduExp1", "EduExp2", "EduExp3"],
    "娱乐性体验": ["EntExp1", "EntExp2", "EntExp3"],
    "逃避性体验": ["EscExp1", "EscExp2", "EscExp3"],
    "审美性体验": ["AesExp1", "AesExp2", "AesExp3"],
    "红色文化认知": ["RCC1", "RCC2", "RCC3"],
    "社会责任感": ["SR1", "SR2", "SR3"],
    "爱国主义情感": ["PC1", "PC2", "PC3"]
}

# 计算 Cronbach's Alpha
alpha_results = {}
for construct, items in constructs.items():
    alpha_results[construct] = cronbach_alpha(data[items])

# 效度分析: 收敛效度（AVE 和 CR）
def calculate_ave_cr(items_scores):
    """Calculate Average Variance Extracted (AVE) and Composite Reliability (CR)."""
    loadings = items_scores.corr().mean(axis=1).values  # Simplified approach for loadings
    ave = np.mean(loadings ** 2)  # Average Variance Extracted
    cr = (sum(loadings) ** 2) / (sum(loadings ** 2) + sum(items_scores.var(axis=0)))  # Composite Reliability
    return ave, cr

ave_cr_results = {}
for construct, items in constructs.items():
    ave_cr_results[construct] = calculate_ave_cr(data[items])

# 输出信度和效度结果
print("Cronbach's Alpha (信度分析):")
for construct, alpha in alpha_results.items():
    print(f"{construct}: {alpha:.2f}")

print("\n收敛效度分析 (AVE 和 CR):")
for construct, (ave, cr) in ave_cr_results.items():
    print(f"{construct}: AVE = {ave:.2f}, CR = {cr:.2f}")
