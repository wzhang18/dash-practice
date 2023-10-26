# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:58:55 2023

@author: weiqi
"""
from dash import Dash, dcc, html, callback, Input, Output
import pandas as pd

data = pd.read_csv('random sample data.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Markdown('''# Sample Report ''')
    
    ])

if __name__ == '__main__':
    app.run(debug = True)