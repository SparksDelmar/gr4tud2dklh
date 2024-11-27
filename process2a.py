import matplotlib.pyplot as plt
import pandas as pd

# Descriptive statistics for each category of experience
categories = {
    "教育性体验": ["EduExp1", "EduExp2", "EduExp3"],
    "娱乐性体验": ["EntExp1", "EntExp2", "EntExp3"],
    "逃避性体验": ["EscExp1", "EscExp2", "EscExp3"],
    "审美性体验": ["AesExp1", "AesExp2", "AesExp3"],
}

# Calculate mean scores for each category
category_means = {
    category: data1[questions].mean(axis=1).mean()
    for category, questions in categories.items()
}

# Visualize the mean scores
plt.bar(category_means.keys(), category_means.values())
plt.title("红色旅游体验各维度平均得分")
plt.ylabel("平均得分")
plt.xlabel("体验维度")
plt.ylim(1, 5)
plt.xticks(rotation=45)
plt.show()

# Generate descriptive insights for each category
education_exp_analysis = data1[categories["教育性体验"]].mean().to_dict()
entertainment_exp_analysis = data1[categories["娱乐性体验"]].mean().to_dict()
escapism_exp_analysis = data1[categories["逃避性体验"]].mean().to_dict()
aesthetic_exp_analysis = data1[categories["审美性体验"]].mean().to_dict()

# Prepare detailed insights into how each category might influence other dimensions
education_exp_analysis, entertainment_exp_analysis, escapism_exp_analysis, aesthetic_exp_analysis
