import pandas as pd

df = pd.read_csv('sampah.csv')
df.dropna(inplace=True)
print(df.to_string())
# Cek data yang sama 
print(df.duplicated())
# Cek data yang sama dan mengganti dengan kata True
df.drop_duplicates(inplace =True) 
print(df.to_string())