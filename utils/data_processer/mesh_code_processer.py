import pandas as pd

def mesh_center(mesh_code):
    # Convert mesh_code to string if it's not already
    mesh_code = str(mesh_code)
    
    # Handle possible missing or invalid mesh codes
    if not mesh_code or len(mesh_code) < 11:
        return None, None
    
    # Function to convert mesh code to latitude and longitude bounds
    def mesh_to_latlon(mesh_code):
        # Extract parts of the mesh code
        lat1 = int(mesh_code[:2]) * 2/3
        lon1 = int(mesh_code[2:4]) + 100
        lat2 = int(mesh_code[4:6]) / 8
        lon2 = int(mesh_code[6:8]) / 8
        
        # 1/2, 1/4, and 1/8 mesh adjustments
        sub_mesh = mesh_code[8:]
        for i, factor in enumerate([1/2, 1/4, 1/8]):
            if len(sub_mesh) > i:
                adjustment = int(sub_mesh[i])
                if adjustment == 1:
                    lat1 += factor * 2/3
                elif adjustment == 2:
                    lon1 += factor
                elif adjustment == 3:
                    lat1 += factor * 2/3
                    lon1 += factor
        
        lat2 /= 60
        lon2 /= 60
        
        lat_min = lat1 + lat2
        lat_max = lat_min + 2/3/60/8
        lon_min = lon1 + lon2
        lon_max = lon_min + 1/60/8
        
        return lat_min, lat_max, lon_min, lon_max

    # Get latitude and longitude bounds
    lat_min, lat_max, lon_min, lon_max = mesh_to_latlon(mesh_code)
    
    # Calculate the center
    lat_center = (lat_min + lat_max) / 2
    lon_center = (lon_min + lon_max) / 2
    
    return lat_center, lon_center