import geopandas as gpd
import pandas as pd
from shapely.geometry import Point


def data_travel_filter_by_region(df, shapefile):
    """
    Keep data that either origin or destination inside shapefile
    """
    # Convert DataFrame to GeoDataFrame with Points geometry
    geometry_origin = [Point(xy) for xy in zip(df['longitude_o'], df['latitude_o'])]
    geometry_destination = [Point(xy) for xy in zip(df['longitude_d'], df['latitude_d'])]

    gdf_origin = gpd.GeoDataFrame(df, geometry=geometry_origin, crs='EPSG:4612')
    gdf_destination = gpd.GeoDataFrame(df, geometry=geometry_destination, crs='EPSG:4612')

    # Spatial join with GeoJSON shapefile
    gdf_origin_within_shape = gpd.sjoin(gdf_origin, shapefile, op='within', how='inner')
    gdf_destination_within_shape = gpd.sjoin(gdf_destination, shapefile, op='within', how='inner')

    # Combine results (keeping only unique rows)
    filtered_gdf = pd.concat([gdf_origin_within_shape, gdf_destination_within_shape]).drop_duplicates()

    # Final DataFrame with filtered rows
    filtered_df = df[df.index.isin(filtered_gdf.index)]

    return filtered_df