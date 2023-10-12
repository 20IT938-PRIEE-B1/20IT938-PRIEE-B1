# Inventory management using Data Analytics

## Problem statement
Retail store handles stock in large scale on daily basis that makes the monitoring and managing of the inventory more tedious. This brings in the need for a digitized inventory management system that performs retail store stock analytics to achieve less inventory on hand and more stocks on sale with less manual labor.

## Proposed solution
The proposed solution addresses the problem in managing the inventory using the time series forecasting algorithm. Out of the different models available in this algorithm, SARIMA (Seasonal Autoregressive Integrated Moving Average) model is preferred as it outperforms the others with the ability to forecast with seasonal time series data. SARIMA when compared with the Holt-Winter's Exponential Smoothing produces smaller MAD (Mean Absolute Deviation) value. This makes SARIMA model feasible to be used for forecasting. SARIMA uses three non-seasonal parameters as p(AR order), d(degree of differencing), q(order of MA) and three seasonal parameters as P(seasonal AR order), D(seasonal differencing), Q(seasonal MA order) that gives the overall evaluation formula as (p,d,q)X(P,D,Q)s. Some of the datasets used in this model are as the sales in a year or a month, seasonal sale of a product which provides insight on seasonal trends and predicts the sales flow in the store. Overall the model predicts the inventory needed to fulfill future customer orders over a period of time. At the end an efficient inventory management system is developed using the SARIMA machine learning model.

