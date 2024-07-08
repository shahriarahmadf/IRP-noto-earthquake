import geopandas as gpd
import folium

def ishikawa_region_mapper():
    """No input.
    Just returns the Ishikawa map shapefile shaded on folium map centering at Ishikawa
    """
    # Centered around Ishikawa prefecture coordinates (approximate)
    ishikawa_center = [36.7199, 136.7365]

    map = folium.Map(location=ishikawa_center, zoom_start=8, tiles='CartoDB positron')

    # Replace 'path_to_your_shapefile.shp' with the actual path to your shapefile
    jpn_adm2 = gpd.read_file('E:\\IRP_noto_earthquake\\data\\raw\\jpn_adm\\jpn_adm_2019_shp\\jpn_admbnda_adm2_2019.shp')
    jpn_adm2.crs = 'EPSG:3857'

    # Filter specific administrative units
    jpn_adm2 = jpn_adm2[
        (jpn_adm2['ADM2_EN'] == 'Suzu City') |
        (jpn_adm2['ADM2_EN'] == 'Anamizu-machi') |
        (jpn_adm2['ADM2_EN'] == 'Noto-cho') |
        (jpn_adm2['ADM2_EN'] == 'Wajima City') |
        (jpn_adm2['ADM2_EN'] == 'Shika-machi') |
        (jpn_adm2['ADM2_EN'] == 'Nanao City')
    ]

    # Buffer function
    def buffer(geometry):
        buffered = geometry.buffer(0.01)  # Adjust buffer distance as needed
        return buffered

    # Apply buffer function to geometries
    jpn_adm2['geometry'] = jpn_adm2['geometry'].apply(buffer)

    # Dissolve based on shared boundaries
    dissolved = jpn_adm2.unary_union

    # Convert dissolved geometry back to GeoDataFrame
    jpn_adm2_dissolved = gpd.GeoDataFrame(geometry=[dissolved], crs=jpn_adm2.crs)

    # Convert GeoDataFrame to GeoJSON
    jpn_adm2_dissolved_geojson = jpn_adm2_dissolved.to_json()

    # Add GeoJSON layer to map with adjusted opacity
    folium.GeoJson(
        jpn_adm2_dissolved_geojson,
        name='Boundary',
        style_function=lambda x: {'fillColor': '#3366cc', 'color': '#3366cc', 'weight': 0.3, 'fillOpacity': 0}  # Adjust fillOpacity here
    ).add_to(map)

    return map, jpn_adm2_dissolved



    # # Replace 'path_to_your_shapefile.shp' with the actual path to your shapefile
    # ishikawa_shp = gpd.read_file('E:\\IRP_noto_earthquake\data\\raw\\ishikawa_boundary_data\\shapefile\\Japan_Prefecture_Boundaries_ECM.shp')
    # ishikawa_shp.crs = 'epsg:3857'



    # # Filter Ishikawa Prefecture
    # ishikawa_prefecture = ishikawa_shp[ishikawa_shp['NAME_1'] == 'Ishikawa'] 

    # # Centered around Ishikawa prefecture coordinates (approximate)
    # ishikawa_center = [36.7199, 136.7365]

    # ishikawa_map = folium.Map(location= ishikawa_center, zoom_start=8, tiles='CartoDB positron')

    # # Convert GeoDataFrame to GeoJSON
    # ishikawa_geojson = ishikawa_prefecture.to_json()

    # # Define a style
    # style_function = lambda x: {'fillColor': '#3366cc', 'color': '#3366cc', 'weight': 1.2, 'fillOpacity': 0.3}

    # # Add GeoJSON layer to map
    # folium.GeoJson(
    #     ishikawa_geojson,
    #     name='Ishikawa Prefecture',
    #     style_function=style_function
    # ).add_to(ishikawa_map)