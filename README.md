# Inventory management using Data Analytics

## Abstract
Analytics is widely used in number of business sectors where it has proven to benefit the management and daily operations. Here the proposed system focuses mainly on the retail sector as stocks are handled in bulk quantites which brings in the need for a digitized system that can analyze and help managing the inventory effectively. Analytics in this sector has become a mandatory supporting component as the business actions and decisions are taken potently and quickly based on it. Here the proposed system uses SARIMA (Seasonal Autoregressive Integrated Moving Average) statistical analysis model for performing the analysis on the retail store data such as the sales history of the retail store, inventory and demand history of the store. Unlike other analytics model, SARIMA has seasonal component and parameters as p (AR order), d(degree of differencing), q(order of MA), P(seasonal AR order), D(seasonal differencing) and Q(seasonal MA order) that helps it in handling seasonal time series data. Also, SARIMA has smaller MAD (Mean Absolute Deviation) value that makes it outperform other time series analytics model. Overall, the model efficiently performs retail store stock inventory analysis and calculates the inventory needed to fullfill the customer requirements over a period of time benefiting the retail store with maximum profit.

## Problem statement
Retail store handles stock in large scale on daily basis that makes the monitoring and managing of the inventory more tedious. This brings in the need for a digitized inventory management system that performs retail store stock analytics to achieve less inventory on hand and more stocks on sale with less manual labor.

## Proposed solution
The proposed solution addresses the problem in managing the inventory using the time series forecasting algorithm. Out of the different models available in this algorithm, SARIMA (Seasonal Autoregressive Integrated Moving Average) model is preferred as it outperforms the others with the ability to forecast with seasonal time series data. SARIMA when compared with the Holt-Winter's Exponential Smoothing produces smaller MAD (Mean Absolute Deviation) value. This makes SARIMA model feasible to be used for forecasting. SARIMA uses three non-seasonal parameters as p(AR order), d(degree of differencing), q(order of MA) and three seasonal parameters as P(seasonal AR order), D(seasonal differencing), Q(seasonal MA order) that gives the overall evaluation formula as (p,d,q)X(P,D,Q)s. Some of the datasets used in this model are as the sales in a year or a month, seasonal sale of a product which provides insight on seasonal trends and predicts the sales flow in the store. Overall the model predicts the inventory needed to fulfill future customer orders over a period of time. At the end an efficient inventory management system is developed using the SARIMA machine learning model.

## Base paper 
Link : https://github.com/20IT938-PRIEE-B1/20IT938-PRIEE-B1/blob/main/Base%20paper.pdf
