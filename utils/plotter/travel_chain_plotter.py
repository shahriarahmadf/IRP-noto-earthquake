import folium
import pandas as pd
import numpy as np

def travel_chain_plotter(map_obj, filtered_df):
    map = map_obj  # Assign map_obj to map for clarity

    # Define colors for different modes
    mode_colors = {
        'car': 'red',
        'walk': 'blue',
        'train': 'yellow',
        'bike': 'purple',
        pd.NA : 'black' 
    }

    # Calculate the maximum stay time for scaling
    max_stay_time = filtered_df['stay_time_o'].max()
    max_circle_radius = 30  # Define the maximum radius for the circles (in meters)

    # Plot circles and polylines for each point from filtered_df
    for index, row in filtered_df.iterrows():
        # Origin circle (latitude_o, longitude_o)
        folium.Circle(
            location=[row['latitude_o'], row['longitude_o']],
            radius=min(row['stay_time_o'] / max_stay_time * max_circle_radius, max_circle_radius),  # Scale radius based on stay time
            popup=f"Origin: {row['common_id']}",
            color='orange', 
            fill=True,
            fill_color='orange', 
        ).add_to(map)
        
        # Destination circle (latitude_d, longitude_d)
        folium.Circle(
            location=[row['latitude_d'], row['longitude_d']],
            radius=min(row['stay_time_d'] / max_stay_time * max_circle_radius, max_circle_radius),  # Scale radius based on stay time
            popup=f"Destination: {row['common_id']}",
            color='green',
            fill=True,
            fill_color='green',
        ).add_to(map)

        # Polyline between origin and destination
        folium.PolyLine(
            locations=[[row['latitude_o'], row['longitude_o']], [row['latitude_d'], row['longitude_d']]],
            color=mode_colors.get(row['mode'], 'gray'),  # Default to gray if mode not defined
            weight=2,  # Adjust weight of polyline
            opacity=0.7  # Adjust opacity of polyline
        ).add_to(map)
    
    return map