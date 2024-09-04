import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
import requests
import csv
from polyline import decode

def get_token():
    #potetial TODO: need to implement a way of updating refresh token
    load_dotenv()
    id = os.getenv("CLIENT_ID")
    secret = os.getenv("CLIENT_SECRET")
    refresh_token = '3c214e2173ed6ef880a3231e12da87e76fa5a192'

    auth_url = "https://www.strava.com/oauth/token"
    data = {
        'client_id' : id,
        'client_secret' : secret,
        'grant_type' : 'refresh_token',
        'refresh_token' : refresh_token
    }

    #request
    auth_result = requests.post(auth_url, data=data).json()
    access_token = auth_result['access_token']
    return access_token

def get_segment_stats(id, access_token):
    request_url = f'https://www.strava.com/api/v3/segments/{id}'
    header = {"Authorization" : "Bearer " + access_token}

    result = requests.get(request_url, headers=header).json()
    
    try:
        return [result['effort_count'], result['athlete_count']]
    except:
        print('Error with id:', id)
        return [0, 0]

def get_all_segment_stats(id_list, access_token):
    #1st ID (acoustic segment) will exist
    norm_stats = get_segment_stats(id_list[1], access_token)
    #if the trail has an alternate ending, add stats from this to the main trail
    if id_list[2]:
        alt_stats = get_segment_stats(id_list[2], access_token)
        norm_stats[0] += alt_stats[0]
        norm_stats[1] += alt_stats[1]
    
    #ebike segments
    ebike_stats = [0, 0] #assume 0 riders
    #if an ebike segment exists
    if id_list[3]:
        ebike_stats = get_segment_stats(id_list[3], access_token)
        #if an alternate ebike segment exists
        if id_list[4]:
            alt_stats = get_segment_stats(id_list[4], access_token)
            ebike_stats[0] += alt_stats[0]
            ebike_stats[1] += alt_stats[1]

    #return array of acoustic bike attempts, ebike attempts, and total unique athletes
    return norm_stats[0], ebike_stats[0], norm_stats[1]+ebike_stats[1]

def append_row(file_path, dict_data):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)
    with open(file_path, 'a', newline='') as csvfile:
        # Get the fieldnames from the dictionary keys
        fieldnames = dict_data.keys()
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header if the file does not exist
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(dict_data)

def get_path(id, access_token):
    request_url = f'https://www.strava.com/api/v3/segments/{id}'
    header = {"Authorization" : "Bearer " + access_token}

    result = requests.get(request_url, headers=header).json()
    
    polyline = result['map']['polyline']

    return decode(polyline)