import pandas as pd
import plotly.express as px

def mode_vs_frequency(df, title= 'Mode of Transport vs Frequency of Travels', xaxis_title='Mode of Transportation',yaxis_title='Frequency of Travels',save_image=False):
    mode_counts = df['mode'].value_counts()

    modes = ['bike', 'car', 'walk', 'train'] 
    for mode in modes:
        if mode not in mode_counts:
            mode_counts[mode] = 0

    # Convert the Series to a DataFrame for Plotly
    mode_counts_df = mode_counts.reset_index()
    mode_counts_df.head()

    # plotly columns
    mode_counts_df.columns = ['mode', 'count']

    # Plotting the histogram using Plotly
    fig = px.bar(mode_counts_df, 
                x='mode', 
                y='count', 
                title=title)
    fig.update_layout(
        width=800,  # Specify the width of the figure
        height=600,  # Specify the height of the figure
        xaxis_title=xaxis_title,  # Label for the x-axis
        yaxis_title=yaxis_title  # Label for the y-axis
    )
    fig.show()

    if save_image == True:
        fig.write_image("E:\\IRP_noto_earthquake\\reports\\mode_vs_frequency.png")
        
    return fig