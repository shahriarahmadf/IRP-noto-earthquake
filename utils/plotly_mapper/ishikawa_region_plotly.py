import geopandas as gpd
import plotly.express as px
import json

def ishikawa_region_plotly():
    """No input.
    Just returns the Ishikawa map shapefile shaded on a Plotly map centered at Ishikawa
    """
    # Replace 'path_to_your_shapefile.shp' with the actual path to your shapefile
    jpn_adm2 = gpd.read_file('E:\\IRP_noto_earthquake\\data\\raw\\jpn_adm\\jpn_adm_2019_shp\\jpn_admbnda_adm2_2019.shp')
    jpn_adm2.crs = 'EPSG:4326'

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
    jpn_adm2_dissolved_geojson = json.loads(jpn_adm2_dissolved.to_json())

    # Create Plotly map
    fig = px.choropleth_mapbox(
        geojson=jpn_adm2_dissolved_geojson,
        locations=[0],  # Using a dummy location, as we are using a single dissolved geometry
        featureidkey="properties.id",  # Dummy feature id key
        color=[1],  # Dummy color, as we are using a single dissolved geometry
        mapbox_style="carto-positron",
        zoom=8,
        center={"lat": 36.7199, "lon": 136.7365},
        opacity=0.5
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return fig
