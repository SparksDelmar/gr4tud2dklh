import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr

# 设置字体和符号显示
plt.rc('font', family='SimHei')
plt.rcParams['axes.unicode_minus'] = False

# 加载本地数据文件
data = pd.read_csv("pls_sem_data.csv")  # 请确保文件路径和名称正确

# 计算相关性矩阵
correlation_matrix = data.corr()

# 绘制美观的热力图
plt.figure(figsize=(12, 10))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="none")
plt.colorbar(label="相关系数")
plt.title("变量相关性矩阵热力图")

# 标注数值
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}",
                 ha='center', va='center', color='black')

# 添加轴标签
plt.xticks(range(len(data.columns)), data.columns, rotation=90)
plt.yticks(range(len(data.columns)), data.columns)

plt.tight_layout()
plt.show()

# 显著性检验
significance_results = {}
for i, col1 in enumerate(data.columns):
    for j, col2 in enumerate(data.columns):
        if i < j:  # 避免重复计算
            corr, p_value = pearsonr(data[col1], data[col2])
            if p_value < 0.05:
                significance_results[f"{col1} 与 {col2}"] = (corr, p_value)

# 输出显著性结果
print("显著相关关系：")
for key, value in significance_results.items():
    print(f"{key}: 相关系数 = {value[0]:.2f}, p值 = {value[1]:.4f}")
