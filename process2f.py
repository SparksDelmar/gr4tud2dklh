import matplotlib.pyplot as plt
import networkx as nx

# 设置中文显示
plt.rc('font', family='SimHei')  # 显示中文字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 数据：根据输出的路径系数和变量命名设置关系
edges = [
    ("红色旅游", "红色文化", 0.948),  # 路径系数
    ("红色旅游", "社会责任", 0.646),
    ("红色文化", "社会责任", 0.267),
    ("红色旅游", "爱国情感", 0.869),
    ("红色文化", "爱国情感", 0.290),
    ("社会责任", "爱国情感", 0.078)
]

# 初始化有向图
G = nx.DiGraph()

# 添加节点
nodes = ["红色旅游", "红色文化", "社会责任", "爱国情感"]
G.add_nodes_from(nodes)

# 添加边和权重（路径系数）
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# 绘图
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)  # 使用弹簧布局生成节点位置

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="lightblue")

# 绘制带箭头的边
nx.draw_networkx_edges(
    G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=2, connectionstyle="arc3,rad=0.2"
)

# 绘制节点标签
nx.draw_networkx_labels(G, pos, font_size=14, font_color="black")

# 添加路径系数（权重）标签
edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=12)

# 图形标题和调整
plt.title("结构方程模型路径图", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.show()
