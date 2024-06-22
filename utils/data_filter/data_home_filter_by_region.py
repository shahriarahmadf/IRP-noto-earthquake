import geopandas as gpd
from shapely.geometry import Point

def data_home_filter_by_region(df, shapefile, wantResidents=False):
    """
    Keep data where home locations are outside the shapefile.
    """
    # Convert DataFrame to GeoDataFrame with Points geometry
    geometry_home = [Point(xy) for xy in zip(df['longitude_h'], df['latitude_h'])]
    gdf_home = gpd.GeoDataFrame(df, geometry=geometry_home, crs='EPSG:3857')

    # Spatial join with GeoJSON shapefile using 'intersects' operation
    gdf_home_within_shape = gpd.sjoin(gdf_home, shapefile, op='intersects', how='inner')

    # Get indices of points within the shapefile
    indices_within_shape = gdf_home_within_shape.index
    
    if wantResidents == False:
        # Filter out rows where the point is within the shapefile
        filtered_df = df[~df.index.isin(indices_within_shape)]

    else:
        filtered_df = df[df.index.isin(indices_within_shape)]

    return filtered_df



# import geopandas as gpd
# import pandas as pd
# from shapely.geometry import Point


# def data_home_travel_filter_by_region(df, jpn_adm2):

#     # Convert DataFrame to GeoDataFrame with Points geometry
#     geometry_home = [Point(xy) for xy in zip(df['longitude_h'], df['latitude_h'])]
#     gdf_home = gpd.GeoDataFrame(df, geometry=geometry_home, crs='EPSG:4326')

#     # Spatial join with GeoJSON shapefile using 'intersects' operation
#     gdf_home_within_shape = gpd.sjoin(gdf_home, jpn_adm2, op='intersects', how='inner')

#     # Get indices of points within the shapefile
#     indices_within_shape = gdf_home_within_shape.index

#     # Filter out rows where the point is within the shapefile
#     filtered_df = df[~df.index.isin(indices_within_shape)]

#     return filtered_df