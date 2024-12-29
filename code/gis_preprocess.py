import pandas as pd
import os

# Specify the folder containing CSV files
folder_path = "C:/Users/fires/Python Projects/UCSC Biking/trail coords"

trail_list = pd.read_csv("C:/Users/fires/Python Projects/UCSC Biking/trail_list.csv", dtype=str)
atheltes = pd.read_csv("C:/Users/fires/Python Projects/UCSC Biking/output/athlete_count.csv", dtype=str)
bikes = pd.read_csv("C:/Users/fires/Python Projects/UCSC Biking/output/pedal_attempts.csv", dtype=str)
ebike = pd.read_csv("C:/Users/fires/Python Projects/UCSC Biking/output/ebike_attempts.csv", dtype=str)

# Iterate through files in the folder
for file_name in os.listdir(folder_path):
    end = file_name.find(".")
    name = file_name[:end]
    
    trail_id = trail_list.loc[trail_list['trail_name'] == name]['trail_id'].values[0]
    riders = int(bikes[trail_id].iloc[-1]) - int(bikes[trail_id].iloc[0])
    ebikers = int(ebike[trail_id].iloc[-1]) - int(ebike[trail_id].iloc[0])

    #write file with lat long name pedal ebike climb region, make name compatible with geodatabase
    trail_coords = pd.read_csv(f"C:/Users/fires/Python Projects/UCSC Biking/trail coords/{name}.csv")
    trail_coords['name'] = name
    trail_coords['pedal_ct'] = riders
    trail_coords['ebike_ct'] = ebikers
    trail_coords['type'] = trail_list.loc[trail_list['trail_name'] == name]['type'].values[0]
    trail_coords['region'] = trail_list.loc[trail_list['trail_name'] == name]['region'].values[0]

    clean_name = name.replace("4 ","Four").replace(" ","_").replace("(","").replace(")","").replace("'","")
    trail_coords.to_csv(f"C:/Users/fires/Python Projects/UCSC Biking/gis_points/{clean_name}.csv")