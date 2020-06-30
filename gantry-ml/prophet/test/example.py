from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot
import pandas as pd
import matplotlib.pyplot as plt

cap = 0.15 
floor = 0.0

df = pd.read_csv("./collect_metric_data/prophet_data.csv")
#df = pd.read_csv("./data/example_wp_log_R.csv")
print(df.head())

df['cap'] = cap
df['floor'] = floor 
m = Prophet() # Defalut growth='linear'
m.fit(df) 
#m = Prophet(growth = 'logistic') 
#m.fit(df)

future = m.make_future_dataframe(periods=25, freq='H')
print(future.tail())
future['cap'] = cap
future['floor'] = floor 

# Trend Chagepoints
#m = Prophet(changepoint_prior_scale = 0.5) 
#forecast = m.fit(df).predict(future)

# 
forecast = m.predict(future) 
#print(forecast.tail())
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)

a = add_changepoints_to_plot(fig1.gca(), m, forecast) 

plt.show()

