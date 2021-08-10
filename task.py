import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

cities_info = []
with open('cities.csv',newline='\n',encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        cities_info.append({"city":row[" city"].strip(),"id": int (row["id"].strip()),"region": int (row[" region"].strip())})

cities_info_name = [city.get("city") for city in cities_info]

def get_city_info(cities):
    return_cities_info = []
    return_cities_name = []
    for city in cities:
        best_city_name_by_ratio = process.extractOne(city["city"], cities_info_name)[0]
        if not(best_city_name_by_ratio in return_cities_name):
           
            return_cities_info.append(cities_info[cities_info_name.index(best_city_name_by_ratio)])
            return_cities_name.append(cities_info[cities_info_name.index(best_city_name_by_ratio)]["city"])
    return return_cities_info

cities = [{"city": "Москва"}, {"city":"Козань"}, {"city":"Казонь"}] 

print(get_city_info(cities))


