import pandas as pd
from shapely.geometry import Point
import geopandas as gpd

import os 
from datetime import datetime
from decode_mesh_code import get_home_locations

def mobility_data_loader(start_date='20240101', end_date='20240101'):
    """
    This function loads the data
    By default, loads only the data of day one
    """
    data_path = 'E:\\IRP_noto_earthquake\\data\\raw\\ishikawa_pref_od\\'

    # print(start_date,end_date)
    temp = False

    # Dataframe
    dataframe_dict = {}
    c=0
    for file_name in os.listdir(data_path):
        c+=1
        print(c)
        if file_name[:8]==start_date:
            temp = True
        
        if temp == True:
            file_path = data_path + file_name
            df = pd.read_csv(file_path)
            
            print(f'{file_name[:8]} dataframe shape')
            print(df.shape)

            # Fix datetime column data type
            df['arrive_time_o'] = pd.to_datetime(df['arrive_time_o'], format='%Y-%m-%d %H:%M:%S')
            df['depart_time_o'] = pd.to_datetime(df['depart_time_o'], format='%Y-%m-%d %H:%M:%S')
            df['arrive_time_d'] = pd.to_datetime(df['arrive_time_d'], format='%Y-%m-%d %H:%M:%S')
            df['depart_time_d'] = pd.to_datetime(df['depart_time_d'], format='%Y-%m-%d %H:%M:%S')

            # Decode home work mesh to locations
            df = get_home_locations(df)

            # # Drop home and work mesh columns
            df.drop(columns=['poi_home'], inplace=True)
            df.drop(columns=['poi_work'], inplace=True)
            df.drop(columns=['mesh_o'], inplace=True)
            df.drop(columns=['mesh_d'], inplace=True)


            # # Create geometry for points
            # geometry_o = [Point(xy) for xy in zip(df['longitude_o'], df['latitude_o'])]
            # geometry_d = [Point(xy) for xy in zip(df['longitude_d'], df['latitude_d'])]
            # geometry_h = [Point(xy) if pd.notna(xy[0]) and pd.notna(xy[1]) else None for xy in zip(df['longitude_h'], df['latitude_h'])]
            # geometry_w = [Point(xy) if pd.notna(xy[0]) and pd.notna(xy[1]) else None for xy in zip(df['longitude_w'], df['latitude_w'])]

            # # Create GeoDataFrame
            # crs = "EPSG:3857"  # WGS84 coordinate system
            # gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry_o)  # Use geometry_o for origin points
            # gdf = gdf.rename_geometry('geometry_o')  # Rename the geometry column to 'geometry_o'

            # # gdf['geometry_o'] = geometry_o  # Add home points as a new geometry column
            # gdf['geometry_d'] = geometry_d  # Add work points as a new geometry column
            # gdf['geometry_h'] = geometry_h  # Add home points as a new geometry column
            # gdf['geometry_w'] = geometry_w  # Add work points as a new geometry column

            # # # Drop columns that are no longer needed
            # columns_to_drop = ['latitude_o', 'longitude_o', 'latitude_d', 'longitude_d', 'latitude_h', 'longitude_h', 'latitude_w', 'longitude_w']
            # gdf.drop(columns=columns_to_drop, inplace=True)

            dataframe_dict[file_name[:8]] = df

        if file_name[:8]==end_date:
            temp = False
            break
        
    return dataframe_dict

