#!/usr/bin/env python3
"""
Module to fetch Star Wars ships that can hold a given number of passengers.
"""

import requests

def availableShips(passengerCount):
    """
    Fetches and returns a list of Star Wars ships that can hold at least
    `passengerCount` passengers.
    
    Args:
        passengerCount (int): Minimum number of passengers the ship should hold.
    
    Returns:
        list: List of ship names that meet the criteria.
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            return []  # Return empty list if API request fails

        data = response.json()
        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0").replace(",", "")
            if passengers.isdigit() and int(passengers) >= passengerCount:
                ships.append(ship["name"])

        url = data.get("next")  # Get next page URL if available

    return ships