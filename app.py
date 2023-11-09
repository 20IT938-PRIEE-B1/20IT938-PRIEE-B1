# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX

data = pd.read_csv("demand_inventory.csv")
print(data.head())
data = data.drop(columns=['Unnamed: 0'])

fig_demand = px.line(data, x='Date',y='Demand',title='Demand Over Time')
fig_demand.write_image("D:/Documents/Activities/PRIEE/Spyder_Code/templates/images/demand_time.jpg")
#plotly.offline.plot(fig_demand, filename="D:/Documents/Activities/PRIEE/Spyder_Code/templates/plot.html")
fig_demand.show()

fig_inventory = px.line(data, x='Date',y='Inventory',title='Inventory Over Time')
fig_inventory.write_image("D:/Documents/Activities/PRIEE/Spyder_Code/templates/images/inventory_time.jpg")
fig_inventory.show()

data['Date'] = pd.to_datetime(data['Date'],format='%Y/%m/%d')
time_series = data.set_index('Date')['Demand']
differenced_series = time_series.diff().dropna()

# Plot ACF and PACF of differenced time series
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(differenced_series, ax=axes[0])
plot_pacf(differenced_series, ax=axes[1])
plt.show()

order = (1, 1, 1)
seasonal_order = (1, 1, 1, 2)
model = SARIMAX(time_series, order=order, seasonal_order=seasonal_order)
model_fit = model.fit(disp=False)

future_steps = 10 #number of days we are going to predict further
predictions = model_fit.predict(len(time_series), len(time_series) + future_steps - 1)
predictions = predictions.astype(int)
print(predictions)

# Create date indices for the future predictions
future_dates = pd.date_range(start=time_series.index[-1] + pd.DateOffset(days=1), periods=future_steps, freq='D')

# Create a pandas Series with the predicted values and date indices
forecasted_demand = pd.Series(predictions, index=future_dates)

# Initial inventory level
initial_inventory = 5500

# Lead time (number of days it takes to replenish inventory)
lead_time = 1

# Service level (probability of not stocking out)
service_level = 0.95

# Calculate the optimal order quantity using the Newsvendor formula
z = np.abs(np.percentile(forecasted_demand, 100 * (1 - service_level)))
order_quantity = np.ceil(forecasted_demand.mean() + z).astype(int)

# Calculate the reorder point
reorder_point = forecasted_demand.mean() * lead_time + z

# Calculate the optimal safety stock
safety_stock = reorder_point - forecasted_demand.mean() * lead_time

# Calculate the total cost (holding cost + stockout cost)
holding_cost = 0.1  # it's different for every business, 0.1 is an example
stockout_cost = 10  # # it's different for every business, 10 is an example
total_holding_cost = holding_cost * (initial_inventory + 0.5 * order_quantity)
total_stockout_cost = stockout_cost * np.maximum(0, forecasted_demand.mean() * lead_time - initial_inventory)

# Calculate the total cost
total_cost = total_holding_cost + total_stockout_cost

print("Optimal Order Quantity:", order_quantity)
print("Reorder Point:", reorder_point)
print("Safety Stock:", safety_stock)
print("Total Cost:", total_cost)

import pickle
pickle.dump(order_quantity,open('models/quantity.pkl','wb'))
pickle.dump(reorder_point,open('models/reorder.pkl','wb'))
pickle.dump(safety_stock,open('models/safety.pkl','wb'))
pickle.dump(fig_demand,open('models/demandplt.pkl','wb'))
pickle.dump(fig_inventory,open('models/inventoryplt.pkl','wb'))
