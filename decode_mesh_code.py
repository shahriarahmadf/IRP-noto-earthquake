def decode_mesh_code(mesh_code):
    """Get latitude and longitude from mesh_code of the dataset"""

    mesh_code = str(int(mesh_code))  # Ensure the mesh code is a string without decimal part

    # Ensure the mesh code is 11 digits
    if len(mesh_code) != 11:
        raise ValueError("Mesh code must be an 11-digit integer.")

    # Parse the mesh code
    p1 = int(mesh_code[:2])   # Latitude (degrees)
    p2 = int(mesh_code[2:4])  # Longitude (degrees)
    p3 = int(mesh_code[4])    # Latitude (1/8 degree)
    p4 = int(mesh_code[5])    # Longitude (1/8 degree)
    p5 = int(mesh_code[6])    # Latitude (1/80 degree)
    p6 = int(mesh_code[7])    # Longitude (1/80 degree)
    p7 = int(mesh_code[8])    # Latitude (1/800 degree)
    p8 = int(mesh_code[9])    # Longitude (1/800 degree)
    p9 = int(mesh_code[10])   # Latitude/Longitude (1/8000 degree)

    # Calculate latitude
    base_latitude = p1 * 2 / 3 + p3 / 12 + p5 / 120 + p7 / 1200 + (p9 // 2) / 12000
    latitude = base_latitude + 0.5 / 12000  # Center of the cell

    # Calculate longitude
    base_longitude = 100 + p2 + p4 / 8 + p6 / 80 + p8 / 800 + (p9 % 2) / 8000
    longitude = base_longitude + 0.5 / 8000  # Center of the cell

    return latitude, longitude

from decode_mesh_code import decode_mesh_code
import pandas as pd

# Function to handle NaN values in poi_home column
def get_lat_lon(mesh_code):
    if pd.isna(mesh_code):
        return pd.NA, pd.NA  # Return pd.NA (Pandas' null value) for latitude and longitude if mesh_code is NaN
    return decode_mesh_code(mesh_code)

def get_home_locations(df):
    """
    This is the function to call.
    """
    # Apply the function to the 'poi_home' column and create new columns 'latitude_h' and 'longitude_h'
    df[['latitude_h', 'longitude_h']] = df['poi_home'].apply(lambda x: pd.Series(get_lat_lon(x)))
    df[['latitude_w', 'longitude_w']] = df['poi_work'].apply(lambda x: pd.Series(get_lat_lon(x)))

    return df