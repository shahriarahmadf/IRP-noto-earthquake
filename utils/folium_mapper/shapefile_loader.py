import folium
import pandas as pd
import geopandas as gpd


def builtup_shapefile(map_obj):
    map = map_obj  # Assign map_obj to map for clarity
    
    shapefile_path = 'E:\\IRP_noto_earthquake\\data\\raw\\jp_map_shp\\builtupp_jpn.shp'
    


    # Load shapefile using geopandas
    gdf = gpd.read_file(shapefile_path)
    
    # Convert to GeoJSON (since Folium accepts GeoJSON)
    geojson_data = gdf.to_crs(epsg='3857').to_json()  

    # Add GeoJSON layer to the map
    folium.GeoJson(
        geojson_data,
        name='builtup_shapefile',  # Name of the layer
        style_function=lambda feature: {
            'fillColor': 'green',  # Fill color of polygons
            'color': 'black',      # Border color of polygons
            'weight': 2,           # Border width in pixels
            'dashArray': '5, 5'    # Dash pattern
        }
    ).add_to(map)
    
    return map

def road_shapefile(map_obj):
    map = map_obj  # Assign map_obj to map for clarity
    shapefile_path = 'E:\\IRP_noto_earthquake\\data\\raw\\jp_map_shp\\roadl_jpn.shp'
    


    # Load shapefile using geopandas
    gdf = gpd.read_file(shapefile_path)
    
    # Convert to GeoJSON (since Folium accepts GeoJSON)
    geojson_data = gdf.to_crs(epsg='3857').to_json()  

    # Add GeoJSON layer to the map
    folium.GeoJson(
        geojson_data,
        name='road_shapefile',  # Name of the layer
        style_function=lambda feature: {
            'fillColor': 'green',  # Fill color of polygons
            'color': 'black',      # Border color of polygons
            'weight': 2,           # Border width in pixels
            'dashArray': '5, 5'    # Dash pattern
        }
    ).add_to(map)
    
    return map