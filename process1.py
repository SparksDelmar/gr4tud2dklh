import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 读取CSV文件
data = pd.read_csv('red_tour_base.csv')

# 设置字体和符号显示
matplotlib.rc('font', family='SimHei')
plt.rcParams['axes.unicode_minus'] = False

# 查看前几行数据
print(data.head())

# 基本信息统计分析
# 性别统计
gender_counts = data['Gender'].value_counts()

# 年级统计
grade_counts = data['Grade'].value_counts()

# 专业统计
major_counts = data['Major'].value_counts()

# 参与次数统计
participation_counts = data['Participation_Count'].value_counts()

# 参与方式统计（因为是多选项，进行拆分计数）
participation_methods = data['Participation_Method'].str.get_dummies(sep=', ').sum().sort_values(ascending=False)

# 绘制统计图表
plt.figure(figsize=(14, 10))

# 性别统计图
plt.subplot(2, 2, 1)
gender_counts.plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('性别分布')
plt.ylabel('人数')
plt.xticks(rotation=0)

# 年级统计图
plt.subplot(2, 2, 2)
grade_counts.plot(kind='bar', color='lightgreen')
plt.title('年级分布')
plt.ylabel('人数')
plt.xticks(rotation=0)

# 专业统计图
plt.subplot(2, 2, 3)
major_counts.plot(kind='bar', color='orange')
plt.title('专业分布')
plt.ylabel('人数')
plt.xticks(rotation=45)

# 参与次数统计图
plt.subplot(2, 2, 4)
participation_counts.plot(kind='bar', color='purple')
plt.title('参与次数分布')
plt.ylabel('人数')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# 参与方式统计图
plt.figure(figsize=(10, 6))
participation_methods.plot(kind='bar', color='teal')
plt.title('参与方式分布')
plt.ylabel('人数')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
