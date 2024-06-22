import folium
import pandas as pd

def home_plotter(map_obj, filtered_df):
    map = map_obj  # Assign map_obj to map for clarity

    # Plot circles for each point from filtered_df
    for index, row in filtered_df.iterrows():
        folium.Circle(
            location=[row['latitude_h'], row['longitude_h']],
            radius=20,  # Adjust radius as needed (in meters)
            popup=f"Home: {row['common_id']}, ( {row['latitude_h']}, {row['longitude_h']} ) ",
            color='black',
            fill=True,
            fill_color='black'
        ).add_to(map)
    
    return map