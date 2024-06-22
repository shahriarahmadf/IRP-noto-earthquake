from folium.plugins import HeatMap
import pandas as pd

def parse_coordinate(coord_str):
    # Find the position of the degree and minute symbols
    deg_index = coord_str.index('°')
    min_index = coord_str.index('′')

    # Extract the degrees and minutes
    degrees = float(coord_str[:deg_index])
    minutes = float(coord_str[deg_index+1:min_index])

    # Convert minutes to degrees
    decimal_degrees = degrees + minutes / 60

    # Check if the coordinate is south
    if 'S' in coord_str:
        decimal_degrees = -decimal_degrees

    # Round to two decimal places
    decimal_degrees = round(decimal_degrees, 3)

    return decimal_degrees

def heat_map(map, dataframe):
    map_obj = map

    # Prepare data for HeatMap
    heat_data = [[row['Latitude'], row['Longitude'], row['M']] for index, row in dataframe.iterrows()]


    # Add HeatMap to map
    HeatMap(heat_data).add_to(map)

    return map 