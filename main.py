from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import datetime as dt


dataset = DataManager()
sheet_data = dataset.getData()
# print(len(sheet_data))
pprint(sheet_data)
# print(sheet_data[1]['iataCode'] =='')
today_date = dt.datetime.now()
flight_search = FlightSearch()
flight_data = FlightData()
departure_city = input("Where would you like to travel from?")
from_city = flight_search.getDestination(departure_city)
for i in range(0, len(sheet_data)):
    if sheet_data[i]['iataCode'] =='':
        sheet_data[i]['iataCode'] = flight_search.getDestination(sheet_data[i]['city'])
    search_data = {
        "fly_from" : from_city,
        "fly_to": sheet_data[i]['iataCode'],
        "date_from ":str(today_date.date().strftime('%d/%m/%Y')),
        "date_to": str((today_date.date() + dt.timedelta(days=180)).strftime('%d/%m/%Y')),
        "nights_in_dst_from":7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "curr": "EUR"
    }
    # print(search_data)
    result_of_search = flight_data.getFlights(search_data)
    sheet_data[i]['lowestPrice'] = result_of_search
    print(sheet_data[i]['city'], ": ", result_of_search)

dataset.update_data()
pprint(sheet_data[3])