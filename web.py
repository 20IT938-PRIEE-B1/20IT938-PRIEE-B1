# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:36:01 2023

@author: LENOVO
"""
from flask import Flask, render_template
import pickle
import plotly

app=Flask(__name__)
order_quantity=pickle.load(open('models/quantity.pkl','rb'))
reorder_point=pickle.load(open('models/reorder.pkl','rb'))
safety_stock=pickle.load(open('models/safety.pkl','rb'))
demand_plot=pickle.load(open('models/demandplt.pkl','rb'))

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/generate')
def generate():
    return render_template('generate.html',o1=order_quantity,o2=reorder_point,o3=safety_stock)

@app.route('/plot')
def plot():
    return render_template('plot.html')
    #return plotly.offline.plot(demand_plot, filename="D:/Documents/Activities/PRIEE/Spyder_Code/templates/plot.html")

if __name__ == "__main__":
    app.run()
    