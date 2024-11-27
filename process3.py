import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'red_tour_feedback.csv'  # Update the path to your local file if needed
data = pd.read_csv(file_path)

# Combine all the positive impact feedback into one string
positive_feedback = " ".join(data['Q22_Positive_Impact'].dropna().tolist())

# Create a word cloud for the positive impact feedback
wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    font_path='C:/Windows/Fonts/simhei.ttf'  # Use the full path to SimHei font to support Chinese characters
).generate(positive_feedback)

# Plot the word cloud for positive feedback
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Impact Feedback Word Cloud')
plt.show()

# Combine all the improvement suggestions into one string
improvement_suggestions = " ".join(data['Q23_Improvement_Suggestions'].dropna().tolist())

# Create a word cloud for the improvement suggestions
wordcloud_improvement = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    font_path='C:/Windows/Fonts/simhei.ttf'  # Use the full path to SimHei font to support Chinese characters
).generate(improvement_suggestions)

# Plot the word cloud for improvement suggestions
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_improvement, interpolation='bilinear')
plt.axis('off')
plt.title('Improvement Suggestions Word Cloud')
plt.show()
