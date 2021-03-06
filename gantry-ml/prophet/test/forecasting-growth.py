from fbprophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/example_wp_log_R.csv') 
print(df.head())
df['cap'] = 8.5

m = Prophet(growth = 'logistic') 
m.fit(df) 

future = m.make_future_dataframe(periods = 1826) 
future['cap'] = 8.5

fcst = m.predict(future) 
fig = m.plot(fcst)
plt.show()

