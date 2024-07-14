# After earthquake happened, if entered to the region
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

def did_enter_the_region(df, shapefile):

    # Convert DataFrame to GeoDataFrame with Points geometry
    geometry_origin = [Point(xy) for xy in zip(df['longitude_o'], df['latitude_o'])]

    gdf_origin = gpd.GeoDataFrame(df, geometry=geometry_origin, crs='EPSG:4612')

    # Spatial join with GeoJSON shapefile
    gdf_origin_within_shape = gpd.sjoin(gdf_origin, shapefile, op='within', how='inner')

    # Final DataFrame with filtered rows
    filtered_df = df[df.index.isin(gdf_origin_within_shape.index)]

    return filtered_df