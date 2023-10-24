# Retail Store Stock Inventory Analytics

## Abstract
Retail sector handles stock in bulk quantities which brings in the need for a digitized system that can analyze and help managing the inventory effectively. Analytics in this sector has become a mandatory supporting component as the business actions and decisions are taken potently and quickly based on it. Here the proposed work uses SARIMA (Seasonal Autoregressive Integrated Moving Average) statistical analysis model for performing the analysis on the retail store data. Data sets used in this model are as the sales history of the store, inventory and demand history of the store. Unlike other data analytics model, SARIMA has seasonal component and uses parameters as p(auto-regressive order), d(degree of differencing), q(moving-average order), P(seasonal AR order), D(seasonal differencing) and Q(seasonal MA order) that help in handling seasonal time series data. Also, SARIMA model has smaller MAD (Mean Absolute Deviation) value when compared to widely used Holt Winter's Exponential Smoothing model which makes it outperform other time series analytics model. Overall, the SARIMA model efficiently performs retail store stock inventory analytics and calculates the inventory needed to fullfill the customer requirements over a period of time benefiting the retail store with maximum profit. 

## Problem statement
Retail store handles stock in large scale on daily basis that makes the monitoring and managing of the inventory more tedious. This brings in the need for a digitized inventory management system that performs retail store stock analytcis to achieve less inventory on hand and more stocks on sale with less manual labor.


## Proposed solution
The proposed solution addresses the problem in managing the retail store inventory using the time series forecasting algorithm. Out of the different models available in this algorithm, SARIMA (Seasonal Autoregressive Integrated Moving Average) model is preferred as it outperforms the others with its ability to forecast future need with past seasonal time series data. SARIMA when compared with the other time series model such as Holt-Winter's Exponential Smoothing model produces smaller MAD (Mean Absolute Deviation) value. This makes SARIMA model feasible to be used for forecasting. SARIMA has three non-seasonal parameters as p(AR order), d(degree of differencing), q(order of MA) and three seasonal parameters as P(seasonal AR order), D(seasonal differencing), Q(seasonal MA order) that are calculated using ACF (Autocorrelation function) and PACF (Partial autocorrelation function). Newsvendor formula is used in the proposed SARIMA model to calculate the optimal order quantity for the inventory. Overall the model predicts the inventory needed to fulfill future customer orders over a period of time with appropriate datasets from the retail store.

## Base Paper
* Title<br>
On the Application of ARIMA and LSTM to Predict Order Demand Based on Short Lead Time and On-Time Delivery Requirements
* Authors<br>
1. Chien-Chih Wang
2. Chun-Hua Chien
3. Amy J. C. Trappey
* Published year<br>
2021
