import folium
import pandas as pd

def destination_plotter(map_obj, filtered_df):

    map = map_obj
    
    # Filter rows where stay_time_d > 60
    filtered_df = filtered_df[filtered_df['stay_time_d'] > 60]
    
    # Plot circles for each point from filtered_df
    for index, row in filtered_df.iterrows():
        stay_time_d = row['stay_time_d']
        
        # Determine color and radius based on stay_time_d
        if stay_time_d < 180:
            color = 'yellow'
            radius = 10
        elif stay_time_d < 360:
            color = 'orange'
            radius = 20
        elif stay_time_d < 1440:
            color = 'red'
            radius = 30
        elif stay_time_d < 10080:
            color = 'red'
            radius = 40
        else:
            color = 'violet'
            radius = 50
        
        # Check if stay overlaps with night sleep hours (assuming 10 pm to 6 am)
        if row['depart_time_d'].hour >= 6:
            # Plot with black border outline
            folium.Circle(
                location=[row['latitude_d'], row['longitude_d']],
                radius=radius,  # Adjust radius as needed (in meters)
                popup=f"{row['common_id']}<br>Stay Time: {stay_time_d} minutes",
                color='black',
                fill=True,
                fill_color=color,
                fill_opacity=0.7,  # Adjust fill opacity if needed
                weight=4,  # Border thickness
                opacity=1  # Border opacity
            ).add_to(map)
        else:
            # Plot without border outline
            folium.Circle(
                location=[row['latitude_d'], row['longitude_d']],
                radius=radius,  # Adjust radius as needed (in meters)
                popup=f"{row['common_id']}<br>Stay Time: {stay_time_d} minutes",
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7  # Adjust fill opacity if needed
            ).add_to(map)
    
    return map