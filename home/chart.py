from plotly.offline import plot
import plotly.graph_objs as go
from home.getdata import getConfTitles,getConfData,getKeywords,getDataFrame
import pandas as pd
import numpy as np
import plotly.express as px

def getBcharts():

    fig = go.Figure(data=[go.Scatter(
    x=[1, 2, 3, 4], y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        opacity=[1, 1, 1, 1],
        size=[40, 60, 80, 100],
    )
    )])
    
    plt_div1=plot(fig,output_type='div')
    return plt_div1
def barChart():
    animals=['2011', '2012', '2019']
    df=getDataFrame()
    df_yearlycount=df.groupby(['year']).id.count().to_frame().reset_index()
    fig1 = px.bar(df_yearlycount, x='year', y='id')
    fig1.update_layout(title_text='No.of papers published per year',yaxis_title="No.of papers")
    #fig1 = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
    #plot(fig, output_type='div')
    plt_div =plot(fig1, output_type='div')
    return plt_div
def dfProcess():
    df=getDataFrame()
    print(df.groupby(['year']).id.count().to_frame().reset_index().columns)
    
#dfProcess()
