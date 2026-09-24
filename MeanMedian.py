import pandas as pd
import numpy as np

df = pd.read_csv('sampah.csv')
rataRata= np.mean(df['produksi_sampah'])
print("Mean dari produksi sampah adalah:", rataRata)