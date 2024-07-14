from utils.folium_mapper.ishikawa_region_mapper import ishikawa_region_mapper
import geopandas as gpd
import numpy as np 
from utils.data_filter.data_home_filter_by_region import data_home_filter_by_region


def city_classification(df):
    japan_shapefile = gpd.read_file('E:\\IRP_noto_earthquake\\data\\raw\\jpn_adm\\jpn_adm_2019_shp\\jpn_admbnda_adm2_2019.shp')
    japan_shapefile.crs = 'EPSG:4612'

    suzu = japan_shapefile[(japan_shapefile['ADM2_EN'] == 'Suzu City')]
    anamizu = japan_shapefile[(japan_shapefile['ADM2_EN'] == 'Anamizu-machi')]
    noto = japan_shapefile[(japan_shapefile['ADM2_EN'] == 'Noto-cho')]
    wajima = japan_shapefile[(japan_shapefile['ADM2_EN'] == 'Wajima City')]
    shika = japan_shapefile[(japan_shapefile['ADM2_EN'] == 'Shika-machi')]
    nanao = japan_shapefile[(japan_shapefile['ADM2_EN'] == 'Nanao City')]
    cities_shapefile = [suzu, anamizu, noto, wajima, shika, nanao]

    # Add column city_name
    df['home_city'] = np.nan 

    buffered = False
    for city_shapefile in cities_shapefile:
        df = data_home_filter_by_region(df, city_shapefile, wantResidents=False, cityName=True, cityBuffered=buffered)

    
    buffered = True
    for city_shapefile in cities_shapefile:
        df = data_home_filter_by_region(df, city_shapefile, wantResidents=False, cityName=True, cityBuffered=buffered)

    return df