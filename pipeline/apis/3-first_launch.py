#!/usr/bin/env python3
import requests
from datetime import datetime

def get_first_launch():
    # SpaceX API URL
    url = "https://api.spacexdata.com/v4/launches"
    
    # Make an HTTP GET request to the SpaceX API
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from SpaceX API")
        return

    # Get the list of launches from the response
    launches = response.json()

    # Sort the launches by the 'date_unix' field (ascending)
    launches.sort(key=lambda launch: launch['date_unix'])

    # Get the first launch
    first_launch = launches[0]

    # Extract necessary information
    launch_name = first_launch['name']
    launch_date = datetime.utcfromtimestamp(first_launch['date_unix']).strftime('%Y-%m-%dT%H:%M:%S%z')
    rocket_name = first_launch['rocket']['name']
    launchpad_name = first_launch['launchpad']['name']
    launchpad_locality = first_launch['launchpad']['locality']

    # Print the result in the required format
    print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

if __name__ == '__main__':
    get_first_launch()
