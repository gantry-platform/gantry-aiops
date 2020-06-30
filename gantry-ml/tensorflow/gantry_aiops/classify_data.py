import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

headers = ['cpu', 'memory']
data = pd.read_csv("../metric_data/metric_data.csv", 
        delimiter=',',
        names=headers)
df = data

model = KMeans(n_clusters = 3, algorithm='auto')
model.fit(df)

y_predict = model.fit_predict(df)
print(y_predict)   #[0 0 0 0 1 1 1]

df['cluster'] =  y_predict 
print(df)
df.to_csv("cluster.csv", header=False)


plt.scatter(df['cpu'], df['memory'], c=y_predict, s=50, cmap='viridis')
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()

