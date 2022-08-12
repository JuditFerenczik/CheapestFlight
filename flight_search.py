import requests
from flight_data   import FlightData
from keys import TE_ENDPOINT, API_KEY


class FlightSearch:

    def getDestination(self, city):
        location_endpoint = f"{TE_ENDPOINT}/locations/query"
        headers = {"apikey": API_KEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        iAta = results[0]["code"]
        #print(iAta)
        return iAta
    def getFlights(self,search_data):
        search_endpoint = f"{TE_ENDPOINT}/search"
        headers = {"apikey": API_KEY}
        # query = {"term": city, "location_types": "city"}
        response = requests.get(url=search_endpoint, headers=headers, params=search_data)
        results = response.json()
        print(results)
        if len(results["data"]) > 0:

            flight_data = FlightData(
                price=results["data"][0]["price"],
                origin_city=results["data"][0]["cityFrom"],
                origin_airport=results["data"][0]["flyFrom"],
                destination_city=results["data"][0]["cityTo"],
                destination_airport=results["data"][0]["flyTo"],
                out_date=results["data"][0]["dTime"] , #.split("T")[0],
                return_date=results["data"][0]["aTime"]    #.split("T")[0]
            )
            print(f"you can travel from {flight_data.origin_city}({flight_data.origin_airport}) to {flight_data.destination_city}({flight_data.destination_airport}) on a price {flight_data.price} from {flight_data.out_date} to {flight_data.return_date}" )
            endres = flight_data  # results["data"][0]["price"]
        else:
            endres = -1
        return endres
