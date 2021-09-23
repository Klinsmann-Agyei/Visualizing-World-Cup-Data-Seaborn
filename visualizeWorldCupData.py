from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("WorldCupMatches.csv")
df_goals = pd.read_csv("goals.csv")

#print(df.head())
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale = 1.25)
f, ax = plt.subplots(figsize = (12,7))
ax = sns.barplot(data = df, x = "Year", y = "Total Goals")
ax.st_title("Average Number Of Goals Scored In World Cup Matches By Year")
f, ax2 = plt.subplots(figsize = (12,7))
ax2 = sns.boxplot(data = df_goals, x = "Year", y = "goals", palette = "Spectral")
ax2.st_title("Visualized Goals")
plt.show()