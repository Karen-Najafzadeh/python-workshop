import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('corona_data.csv')

df.plot()

plt.show()