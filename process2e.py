import pandas as pd
from semopy import Model
import matplotlib.pyplot as plt

# 加载数据
data_path = "pls_sem_data.csv"  # 替换为实际路径
data = pd.read_csv(data_path)

# 定义结构方程模型
model_description = """
# 潜变量定义
RedTour =~ EduExp1 + EduExp2 + EduExp3 + EntExp1 + EntExp2 + EntExp3 + AesExp1 + AesExp2 + AesExp3
RedCulture =~ RCC1 + RCC2 + RCC3
SocialResp =~ SR1 + SR2 + SR3
Patriotism =~ PC1 + PC2 + PC3

# 路径关系
RedCulture ~ RedTour
SocialResp ~ RedTour + RedCulture
Patriotism ~ RedTour + RedCulture + SocialResp
"""

# 创建 SEM 模型并加载数据
model = Model(model_description)
model.load_dataset(data)

# 拟合模型
model.fit()

# 输出路径系数
print("路径系数和显著性结果：")
results = model.inspect()  # 获取模型路径系数和统计信息
print(results)

# 替代计算拟合指标的代码（如需要更多统计指标，可以启用 calc_stats）
print("\n无法直接计算卡方统计量，以下是替代的拟合结果信息：")
try:
    fit_stats = model.calc_stats()
    print("模型拟合统计：")
    for key, value in fit_stats.items():
        print(f"{key}: {value}")
except AttributeError:
    print("无法计算拟合统计量，可能与当前库版本有关。")

# 可视化路径图（简单替代方法，不使用无效的参数）
try:
    model.plot(path="model_diagram.png")  # 保存模型图
    print("模型路径图已保存为 'model_diagram.png'")
except Exception as e:
    print("可视化路径图时出错：", e)
