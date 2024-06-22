from datetime import datetime
import pandas as pd

def convert_times_into_datetimes(dataframe):
  """
  Convert all arrive time, stay times of origin and destination into datetime
  """


  dataframe['arrive_time_o'] = pd.to_datetime(dataframe['arrive_time_o'], format='%Y-%m-%d %H:%M:%S')
  dataframe['depart_time_o'] = pd.to_datetime(dataframe['depart_time_o'], format='%Y-%m-%d %H:%M:%S')
  dataframe['arrive_time_d'] = pd.to_datetime(dataframe['arrive_time_d'], format='%Y-%m-%d %H:%M:%S')
  dataframe['depart_time_d'] = pd.to_datetime(dataframe['depart_time_d'], format='%Y-%m-%d %H:%M:%S')

  return dataframe
