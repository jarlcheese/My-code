import pandas as pd #analyze csv file
import matplotlib.pyplot as plt #graph generator

surveys_df = pd.read_csv("projects/data/surveys.csv")  #define surveys_df
species_counts = surveys_df.groupby('species_id')['record_id'].count() #define species_counts (attribute variable)

print(species_counts) #for cross reference

species_counts.plot(kind="bar") #plot generation; can use any kind
plt.xlabel('Species ID')
plt.ylabel ('Counts')
plt.title('Species Counts by Species ID')
plt.show()

