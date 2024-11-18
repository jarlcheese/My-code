import pandas as pd
import matplotlib.pyplot as plt

try:
    surveys_df = pd.read_csv("projects/data/surveys.csv")  #define surveys_df
except FileNotFoundError:
    print("FILE NOT FOUND. CHECK DATA PATH")
    exit()

surveys_df['weight'] = pd.to_numeric(surveys_df['weight'], errors='coerce')
surveys_df.dropna(subset=['weight'], inplace=True)

avg_species_weight = surveys_df.groupby('plot_id')['weight'].mean()

avg_species_weight.plot(kind="bar")
plt.xlabel('Plot')
plt.ylabel('Average Weight')
plt.title('Average Weight Per Plot')
plt.tight_layout()
plt.show()