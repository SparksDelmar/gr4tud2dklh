import pandas as pd
from sklearn.decomposition import PCA

# 加载数据
data_path = "pls_sem_data.csv"  
data = pd.read_csv(data_path)

# 进行 Harman 单因子检验（探索性因子分析）
pca = PCA()
pca.fit(data)

# 提取解释方差比例
explained_variance = pca.explained_variance_ratio_

# 计算单因子解释的方差
single_factor_variance = explained_variance[0] * 100  # 转换为百分比
cumulative_variance = explained_variance.cumsum() * 100  # 累计解释方差百分比

# 输出结果
print(f"单因子解释的方差比例: {single_factor_variance:.2f}%")
print("各主成分的累计解释方差比例:")
for i, var in enumerate(cumulative_variance):
    print(f"主成分 {i + 1}: 累计解释方差 {var:.2f}%")
