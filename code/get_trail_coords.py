#for each trail id in the list:

#get the first trail id
#query the polyline
#decode the polyline to a coord set

#write a csv file for each trail's polyline (title with trail name?
#x field, y field use the right coordinate system
from api_query_funcs import get_token, get_path
import csv
from time import sleep

token = get_token()
trail_list = 'C:/Users/fires/Python Projects/UCSC Biking/trail_list.csv'
output_folder = 'C:/Users/fires/Python Projects/UCSC Biking/trail coords'

with open(trail_list, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader, None) #skip header

    for trail in reader:
        
        id = trail[1]
        data = get_path(id, token)
        output_path = f'{output_folder}/{trail[0]}.csv'

        with open(output_path, mode='w', newline='') as file: #write a file for coordinates of each trail
            writer = csv.writer(file)
            #Write header
            writer.writerow(['lat', 'long'])
            writer.writerows(data)

        sleep(18) #avoid rate limiting