import requests
from keys import API_KEY, TE_ENDPOINT


class FlightData:

    def getFlights(self,search_data):
        search_endpoint = f"{TE_ENDPOINT}/search"
        headers = {"apikey": API_KEY}
        # query = {"term": city, "location_types": "city"}
        response = requests.get(url=search_endpoint, headers=headers, params=search_data)
        results = response.json()
        if len(results["data"]) > 0:
            endres = results["data"][0]["price"]
        else:
            endres = -1
        return endres
