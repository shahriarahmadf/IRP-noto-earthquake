import folium
import pandas as pd
import numpy as np

def destination_plotter(map_obj, filtered_df):

    map = map_obj
    
    # Filter rows where stay_time_d > 60
    filtered_df = filtered_df[filtered_df['stay_time_d'] > 60]
    
    # Define colormap and normalization for stay_time_d values
    colormap = 'YlOrRd'  # Choose any colormap from Matplotlib or Folium
    vmin, vmax = filtered_df['stay_time_d'].min(), filtered_df['stay_time_d'].max()
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)  # Use mpl.colors.Normalize for normalization
    
    # Add a colorbar legend
    colormap = folium.colormap.LinearColormap(colors=['yellow', 'red'], vmin=vmin, vmax=vmax)
    colormap.caption = 'Stay Time (minutes)'
    map.add_child(colormap)
    
    # Plot circles for each point from filtered_df
    for index, row in filtered_df.iterrows():
        # Determine color based on normalized stay_time_d
        color = colormap(norm(row['stay_time_d']))
        
        # Plot the circle with color
        folium.Circle(
            location=[row['latitude_d'], row['longitude_d']],
            radius=20,  # Adjust radius as needed (in meters)
            popup=f"Home: {row['common_id']}<br>Stay Time: {row['stay_time_d']} minutes",
            color=color,
            fill=True,
            fill_color=color
        ).add_to(map)
    
    return map