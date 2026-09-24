import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('GRAPE_QUALITY.csv')   

dF = df.dropna(subset=['quality_score', 'sugar_content_brix'])
print(dF.to_string())

plt.scatter(df['quality_score'], df['sugar_content_brix'])
plt.xlabel('Quality Score')
plt.ylabel('Sugar Content (Brix)')
plt.title('Grape Quality vs Quality Score')
plt.show()