import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

df = pd.DataFrame([
    [2, 1],
    [3, 2],
    [3, 4],
    [5, 5],
    [7, 5],
    [2, 5],
    [8, 9],
    [9, 10],
    [6, 12],
    [9, 2],
    [6, 10],
    [2, 4]
], columns = ['hour', 'attendance'])

model = KMeans(n_clusters = 2)
model.fit(df)

y_predict = model.fit_predict(df)
print(y_predict)   #[0 0 0 2 2 0 1 1 1]

df['cluster'] =  y_predict 
print(df)
#df.to_csv("cluster.csv")

#plt.scatter(df['hour'], y_predict, df['attendance'], c='blue')
plt.scatter(df['hour'], df['attendance'], c=y_predict, s=50, cmap='viridis')

centers=model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
#plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=100, marker='D', c='red', label = 'Centroids')
plt.show()

