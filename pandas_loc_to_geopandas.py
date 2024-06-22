import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

import os 
from datetime import datetime
from decode_mesh_code import get_home_locations

def pandas_loc_to_geopandas(df):

    # Create geometry for points
    geometry_o = [Point(xy) for xy in zip(df['longitude_o'], df['latitude_o'])]
    geometry_d = [Point(xy) for xy in zip(df['longitude_d'], df['latitude_d'])]
    geometry_h = [Point(xy) if pd.notna(xy[0]) and pd.notna(xy[1]) else None for xy in zip(df['longitude_h'], df['latitude_h'])]
    geometry_w = [Point(xy) if pd.notna(xy[0]) and pd.notna(xy[1]) else None for xy in zip(df['longitude_w'], df['latitude_w'])]

    # Create GeoDataFrame
    crs = "EPSG:3857"  # WGS84 coordinate system
    gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry_o)  # Use geometry_o for origin points
    gdf = gdf.rename_geometry('geometry_o')  # Rename the geometry column to 'geometry_o'

    # gdf['geometry_o'] = geometry_o  # Add home points as a new geometry column
    gdf['geometry_d'] = geometry_d  # Add work points as a new geometry column
    gdf['geometry_h'] = geometry_h  # Add home points as a new geometry column
    gdf['geometry_w'] = geometry_w  # Add work points as a new geometry column

    # # Drop columns that are no longer needed
    columns_to_drop = ['latitude_o', 'longitude_o', 'latitude_d', 'longitude_d', 'latitude_h', 'longitude_h', 'latitude_w', 'longitude_w']
    gdf.drop(columns=columns_to_drop, inplace=True)