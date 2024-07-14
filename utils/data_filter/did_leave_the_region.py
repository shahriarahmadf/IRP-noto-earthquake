# Before earthquake happened, if left the region
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

def did_leave_the_region(df, shapefile):
    """
    
    """

    # Convert DataFrame to GeoDataFrame with Points geometry
    geometry_destination = [Point(xy) for xy in zip(df['longitude_d'], df['latitude_d'])]

    gdf_destination = gpd.GeoDataFrame(df, geometry=geometry_destination, crs='EPSG:4612')

    # Spatial join with GeoJSON shapefile
    gdf_destination_within_shape = gpd.sjoin(gdf_destination, shapefile, op='within', how='inner')

    # Final DataFrame with filtered rows
    filtered_df = df[df.index.isin(gdf_destination_within_shape.index)]

    return filtered_df