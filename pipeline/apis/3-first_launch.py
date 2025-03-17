import requests
from datetime import datetime

def get_first_launch():
    """
    Fetches the first SpaceX launch from the API and prints its details.
    The launch information includes name, date, rocket, and launchpad.
    """
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    launches = response.json()

    # Sort by launch date (ascending order)
    first_launch = min(launches, key=lambda x: x['date_unix'])

    # Extract information for the first launch
    launch_name = first_launch['name']
    launch_date = datetime.strptime(first_launch['date_local'], "%Y-%m-%dT%H:%M:%S%z")
    rocket_name = first_launch['rocket']
    launchpad_name = first_launch['launchpad']

    # Fetch rocket and launchpad details
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_name}"
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_name}"

    rocket_response = requests.get(rocket_url)
    launchpad_response = requests.get(launchpad_url)

    rocket_data = rocket_response.json()
    launchpad_data = launchpad_response.json()

    rocket_name = rocket_data['name']
    launchpad_name = launchpad_data['name']
    launchpad_locality = launchpad_data['locality']

    # Format the output as requested
    formatted_output = f"{launch_name} ({launch_date.strftime('%Y-%m-%dT%H:%M:%S%z')}) {rocket_name} - {launchpad_name} ({launchpad_locality})"
    print(formatted_output)


if __name__ == '__main__':
    get_first_launch()
