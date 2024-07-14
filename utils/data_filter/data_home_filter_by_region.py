import geopandas as gpd
from shapely.geometry import Point
import pandas as pd

def data_home_filter_by_region(df, shapefile, wantResidents=False, cityName=False, cityBuffered=False):
    """
    Keep data where home locations are outside the shapefile.
    """
    # Drop rows with NaN values in 'longitude_h' or 'latitude_h'
    df = df.dropna(subset=['longitude_h', 'latitude_h'])

    # Convert DataFrame to GeoDataFrame with Points geometry
    geometry_home = [Point(xy) for xy in zip(df['longitude_h'], df['latitude_h'])]
    gdf_home = gpd.GeoDataFrame(df, geometry=geometry_home, crs='EPSG:4612')

    
    if cityBuffered == True:
        city_name = shapefile['ADM2_EN'].iloc[0]
        # Buffer function
        def buffer(geometry):
            buffered = geometry.buffer(0.01)  # Adjust buffer distance as needed
            return buffered

        # Apply buffer function to geometries
        shapefile['geometry'] = shapefile['geometry'].apply(buffer)

        # Dissolve based on shared boundaries
        dissolved = shapefile.unary_union

        # Convert dissolved geometry back to GeoDataFrame
        shapefile = gpd.GeoDataFrame(geometry=[dissolved], crs=shapefile.crs)

    # Spatial join with GeoJSON shapefile using 'intersects' operation
    gdf_home_within_shape = gpd.sjoin(gdf_home, shapefile, op='intersects', how='inner')

    # Get indices of points within the shapefile
    indices_within_shape = gdf_home_within_shape.index
    
    if cityName:
        if cityBuffered == False:
            city_name = shapefile['ADM2_EN'].iloc[0]
        # Update 'home_city' only if it is NaN or empty
        df.loc[indices_within_shape, 'home_city'] = df.loc[indices_within_shape, 'home_city'].apply(
            lambda x: city_name if pd.isna(x) or x == '' else x
        )
        return df

    # Add other logic if needed when wantResidents is True
    # Example: If wantResidents, filter the DataFrame to keep only those inside the shapefile
    if wantResidents:
        return df.loc[indices_within_shape]
    else:
        return df.drop(indices_within_shape)

# recent 14 july 2024 commented

# def data_home_filter_by_region(df, shapefile, wantResidents=False):
#     """
#     Keep data where home locations are outside the shapefile.
#     """
#     # Drop rows with NaN values in 'longitude_h' or 'latitude_h'
#     df = df.dropna(subset=['longitude_h', 'latitude_h'])

#     # Convert DataFrame to GeoDataFrame with Points geometry
#     geometry_home = [Point(xy) for xy in zip(df['longitude_h'], df['latitude_h'])]
#     gdf_home = gpd.GeoDataFrame(df, geometry=geometry_home, crs='EPSG:4612')

#     # Spatial join with GeoJSON shapefile using 'intersects' operation
#     gdf_home_within_shape = gpd.sjoin(gdf_home, shapefile, op='intersects', how='inner')

#     # Get indices of points within the shapefile
#     indices_within_shape = gdf_home_within_shape.index
    
#     if wantResidents == False:
#         # Filter out rows where the point is within the shapefile
#         filtered_df = df[~df.index.isin(indices_within_shape)]

#     else:
#         filtered_df = df[df.index.isin(indices_within_shape)]

#     return filtered_df



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