import pandas as pd
import plotly.express as px

def mode_vs_avgdistance(df, title= 'Average Distance (OD) vs Mode of Transportation', xaxis_title='Mode of Transportation',yaxis_title='Average Distance (Origin-Destination) [km]',save_image=False):

    # Ensure all modes are included
    all_modes = ['car', 'train', 'walk', 'bike']
    missing_modes = [{'mode': mode, 'distance_od': 0} for mode in all_modes if mode not in df['mode'].values]
    df = pd.concat([df, pd.DataFrame(missing_modes)], ignore_index=True)


    # Group by mode and sum only the distance_od column
    df_grouped = df.groupby('mode', as_index=False)['distance_od'].mean()

    # Create the Plotly bar chart
    fig = px.bar(df_grouped, x='mode', y='distance_od', title=title)
    
    fig.update_layout(
        width=800,  # Specify the width of the figure
        height=600,  # Specify the height of the figure
        xaxis_title=xaxis_title,  # Label for the x-axis
        yaxis_title=yaxis_title  # Label for the y-axis
    )
    # Show the plot
    fig.show()

    if save_image == True:
        fig.write_image("E:\\IRP_noto_earthquake\\reports\\mode_vs_avgdistance.png")
        
    return fig