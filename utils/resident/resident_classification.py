# Resident classification
from utils.folium_mapper.ishikawa_region_mapper import ishikawa_region_mapper
from utils.data_filter.data_home_filter_by_region import data_home_filter_by_region
from utils.data_filter.data_travel_filter_by_region import data_travel_filter_by_region
import pandas as pd

def resident_classification(whole_dataframe):
    resident_list = []
    
    for date, df in whole_dataframe.items():

        _, jpn_adm2 = ishikawa_region_mapper()

        # Get travels whose travel also inside study area only
        df = data_travel_filter_by_region(df, jpn_adm2)      

        # Drop rows where 'longitude_h' or 'latitude_h' is NA
        df_with_homes = df.dropna(subset=['longitude_h', 'latitude_h'])

        # Get travels whose home inside study area
        df_home_inside_study_area = data_home_filter_by_region(df_with_homes, jpn_adm2, wantResidents = True)

        # Get Residents List
        resident_common_ids = df_home_inside_study_area['common_id'].unique().tolist()

        resident_list = resident_list + resident_common_ids
        
    resident_list = set(resident_list)

    # Convert the list to a DataFrame with the column name 'common_id'
    resident_list_df = pd.DataFrame(resident_list, columns=['common_id'])
    # Save data of tourists ids
    csv_save_path = 'E:\\IRP_noto_earthquake\\data\\processed\\residents_common_ids.csv'
    resident_list_df.to_csv(csv_save_path, index = False)

    return resident_list_df

def keep_resident_travels_in_df(df):

    _, jpn_adm2 = ishikawa_region_mapper()

    # Get travels whose travel also inside study area only
    df = data_travel_filter_by_region(df, jpn_adm2)      

    # Drop rows where 'longitude_h' or 'latitude_h' is NA
    df_with_homes = df.dropna(subset=['longitude_h', 'latitude_h'])

    # Get travels whose home inside study area
    df_home_inside_study_area = data_home_filter_by_region(df_with_homes, jpn_adm2, wantResidents = True)

    return df_home_inside_study_area
    