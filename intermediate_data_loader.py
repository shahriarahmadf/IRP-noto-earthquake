import os 
import pandas as pd 

def intermediate_data_loader(start_date, end_date):
    data_path = 'E:\\IRP_noto_earthquake\\data\\intermediate\\'

    temp = False

    dataframe_dict = {}
    c=0
    for file_name in os.listdir(data_path):
        c+=1
        print(c)
        if file_name==start_date:
            temp = True
        
        if temp == True:
            file_path = data_path + file_name
            df = pd.read_csv(file_path)
            print(f'{file_name}')

            # Fix datetime column data type
            df['arrive_time_o'] = pd.to_datetime(df['arrive_time_o'], format='%Y-%m-%d %H:%M:%S')
            df['depart_time_o'] = pd.to_datetime(df['depart_time_o'], format='%Y-%m-%d %H:%M:%S')
            df['arrive_time_d'] = pd.to_datetime(df['arrive_time_d'], format='%Y-%m-%d %H:%M:%S')
            df['depart_time_d'] = pd.to_datetime(df['depart_time_d'], format='%Y-%m-%d %H:%M:%S')

            dataframe_dict[file_name] = df

        if file_name==end_date:
            temp = False
            break
        
    return dataframe_dict