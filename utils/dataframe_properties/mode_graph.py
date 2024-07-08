import pandas as pd
import plotly.express as px

def mode_graph(df):
    # Sample DataFrame creation (replace this with your actual DataFrame)


    # Plotting the histogram
    fig = px.histogram(df, x='mode', title='Mode of Transport')

    # Show the plot
    fig.show()
