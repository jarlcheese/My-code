import pandas as pd
import matplotlib.pyplot as plt

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
my_df = pd.DataFrame(d)
print(my_df)

my_df.plot(kind='bar', stacked=True)

plt.title=('Stacked Graph')
plt.show()