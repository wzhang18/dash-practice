# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:58:55 2023

@author: weiqi
"""
from dash import Dash, dcc, html, callback, Input, Output
import pandas as pd
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/wzhang18/dash-practice/main/random%20sample%20data.csv')

app = Dash(__name__)
server = app.server # required for render.com deployment

app.layout = html.Div([
    dcc.Markdown('''# Sample Report '''),
    dcc.Markdown(''' Choose a Role '''),
    dcc.Dropdown(
        options = data['Position'].unique(),
        value = [],
        multi = True,
        id = 'position'
        ),
    dcc.Markdown(''' Choose a Question '''),
    dcc.Dropdown(
        options = data.columns[21:-1],
        value = (),
        id = 'question'
        ),
    #dcc.Graph(
     #   figure = fig2
      #  ),
    dcc.Graph(
        id = 'graph'
        )
    ])

@callback(
    Output(component_id = 'graph', component_property = 'figure'),
    Input(component_id = 'position', component_property = 'value'),
    Input(component_id= 'question', component_property= 'value'),
    prevent_initial_call=True 
    )
def graph(positions, question):
    df = data[data['Position'].isin(positions)]
    groupeddf = pd.crosstab(df['Position'], df[question], normalize = 'index')
    fig = px.bar(groupeddf, x=groupeddf.index, y = groupeddf.columns, text_auto= '.1%')
    return fig


if __name__ == '__main__':
    app.run(debug = True)
