import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Automobile_clean.csv")
print(df.describe())
# MPG distribution (histogram + KDE)
plt.figure(figsize=(6, 4))
sns.histplot(df['mpg'], kde=True, color='indigo')
plt.title('MPG Distribution')
plt.savefig("eda_1_mpg_dist.png", dpi=130, bbox_inches='tight')
plt.show()
#
plt.figure(figsize=(6, 5))
corr = df[['mpg', 'cylinders', 'displacement', 'horsepower',
           'weight', 'acceleration']].corr()
sns.heatmap(corr, annot=True, cmap='Purples', fmt='.2f')
plt.title('Correlation Matrix')
plt.savefig("eda_2_corr.png", dpi=130, bbox_inches='tight')
plt.show()
#The relationship between weight and MPG, colored by country of origin.
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='weight', y='mpg', hue='origin', palette='viridis')
plt.title('Weight vs MPG by Origin')
plt.savefig("eda_3_weight_mpg.png", dpi=130, bbox_inches='tight')
plt.show()
#MPG distribution by country of origin
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='origin', y='mpg', hue='origin', palette='Purples', legend=False)
plt.title('MPG Distribution by Origin')
plt.savefig("eda_4_mpg_by_origin.png", dpi=130, bbox_inches='tight')
plt.show()
#Number of cars by number of cylinders
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='cylinders', color='indigo')
plt.title('Car Count by Cylinders')
plt.savefig("eda_5_cylinders_count.png", dpi=130, bbox_inches='tight')
plt.show()
#Evolution of average MPG over the years
plt.figure(figsize=(7, 4))
yearly = df.groupby('model_year_full')['mpg'].mean().reset_index()
sns.lineplot(data=yearly, x='model_year_full', y='mpg', marker='o', color='indigo')
plt.title('MPG Trend Over Years')
plt.savefig("eda_6_mpg_trend.png", dpi=130, bbox_inches='tight')
plt.show()