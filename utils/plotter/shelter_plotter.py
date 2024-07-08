import folium
import pandas as pd
from utils.data_loader.shelter_data_loader import shelter_data_load

def shelter_plotter(map_obj):
    map = map_obj  # Assign map_obj to map for clarity

    # Get shelter data
    wajima_designated_evacuation_shelters = shelter_data_load()

    # Define the radius for shelter zones (in meters)
    radius = 100

    # Iterate over the evacuation centers dictionary and add markers to the map
    for shelter, coords in wajima_designated_evacuation_shelters.items():
        print(shelter,coords)
        folium.Circle(
            location=coords,
            color='purple',
            fill=True,
            fill_color='purple',
            fill_opacity=0.05,
            tooltip=shelter,
            radius=radius
        ).add_to(map)

        # Add shelter name as a label on the map with fixed size
        folium.Marker(
            location=coords,
            icon=folium.DivIcon(
                icon_size=(150,30),  # Width and height of the icon
                icon_anchor=(75,15),  # Position of the icon relative to the marker location
                html=f'<div style="font-size: 10pt; color: black; position: absolute; width: 150px; text-align: center; pointer-events: none;">{shelter}</div>'
            )
        ).add_to(map)

    return map