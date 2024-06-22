import folium
import pandas as pd

def travel_plotter(map_obj, filtered_df):
    map = map_obj  # Assign map_obj to map for clarity

    # Plot circles for each point from filtered_df
    for index, row in filtered_df.iterrows():
        # Origin circle (latitude_o, longitude_o)
        folium.Circle(
            location=[row['latitude_o'], row['longitude_o']],
            radius=15,  # Adjust radius as needed (in meters)
            popup=f"Origin: {row['common_id']}",
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(map)
        
        # Destination circle (latitude_d, longitude_d)
        folium.Circle(
            location=[row['latitude_d'], row['longitude_d']],
            radius=15,  # Adjust radius as needed (in meters)
            popup=f"Destination: {row['common_id']}",
            color='green',
            fill=True,
            fill_color='green'
        ).add_to(map)

        # Polyline between origin and destination
        folium.PolyLine(
            locations=[[row['latitude_o'], row['longitude_o']], [row['latitude_d'], row['longitude_d']]],
            color='purple',
            weight=0.3,
            opacity=1
        ).add_to(map)
    
    return map