import csv
from time import sleep
from api_query_funcs import get_token, get_all_segment_stats, append_row
from datetime import date
        
trail_list = 'C:/Users/fires/Python Projects/UCSC Biking/trail_list.csv'
output_path = 'C:/Users/fires/Python Projects/UCSC Biking/output'

access_token = get_token()
print("Token aquired.")
#TODO: import csv with ids
#write a list for every stat with an entry for each trail
#write each list to respective file

with open(trail_list, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader, None) #skip header
    
    today = date.today()
    pedal_attempts = {'date' : today}
    e_attempts = {'date' : today}
    athlete_count = {'date' : today}

    count = 0

    print("Reading input file")
    for trail in reader:
        #progress checking
        count += 1
        if count % 4 == 0:
            print(f'{(count/81)*100:.2f}% complete')

        stats = get_all_segment_stats(trail, access_token)
        sleep(18) #avoid rate limit
        
        #for each main segment id, assign a value in each dictionary for the stat
        pedal_attempts[trail[1]] = stats[0]
        e_attempts[trail[1]] = stats[1]
        athlete_count[trail[1]] = stats[2]

    append_row(output_path + '/pedal_attempts.csv', pedal_attempts)
    append_row(output_path + '/ebike_attempts.csv', e_attempts)
    append_row(output_path + '/athlete_count.csv', athlete_count)

print("Output files written.")