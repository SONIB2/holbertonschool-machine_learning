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

    # Debugging: print the first launch to inspect its structure
    print("First Launch Data:", first_launch)

    # Extract necessary information
    try:
        launch_name = first_launch['name']
        launch_date = datetime.utcfromtimestamp(first_launch['date_unix']).strftime('%Y-%m-%dT%H:%M:%S%z')
        
        # Check if rocket is a dictionary and if the 'name' exists within it
        rocket_data = first_launch['rocket']
        if isinstance(rocket_data, dict):
            rocket_name = rocket_data['name']
        else:
            print("Error: 'rocket' field is not a dictionary:", rocket_data)
            return
        
        launchpad_data = first_launch['launchpad']
        if isinstance(launchpad_data, dict):
            launchpad_name = launchpad_data['name']
            launchpad_locality = launchpad_data['locality']
        else:
            print("Error: 'launchpad' field is not a dictionary:", launchpad_data)
            return
        
        # Print the result in the required format
        print(f"{launch_name} ({launch_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})")
    
    except KeyError as e:
        print(f"Error: Missing key {e} in launch data.")
    except TypeError as e:
        print(f"Error: Type error - {e}")

if __name__ == '__main__':
    get_first_launch()
