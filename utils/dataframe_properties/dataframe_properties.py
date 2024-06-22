
def get_number_of_unique_common_ids(df):
    # Count the number of unique common_id values in df_na_home
    number = df['common_id'].nunique()

    return number