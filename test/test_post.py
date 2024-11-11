import requests


data = [{
    'rooms': 2,
    'region': 'Орджоникидзевский',
    'floor': 9,
    'total_area': 56.2,
    'living_area': 30.2,
    'kitchen_area': 8.5,
    'floors_total': 10
}]

data_arr = [
    {
        'rooms': 3,
        'region': 'Орджоникидзевский',
        'floor': 6,
        'total_area': 105.0,
        'living_area': 78.0,
        'kitchen_area': 14.0,
        'floors_total': 9,
    },
    {
        'rooms': 4,
        'region': 'Орджоникидзевский',
        'floor': 9,
        'total_area': 79.0,
        'living_area': 52.7,
        'kitchen_area': 8.2,
        'floors_total': 9
    },
    {
        'rooms': 3,
        'region': 'Орджоникидзевский',
        'floor': 8,
        'total_area': 80.0,
        'living_area': 53.0,
        'kitchen_area': 9.0,
        'floors_total': 9,
    },
    {
        'rooms': 2,
        'region': 'Ленинский',
        'floor': 2,
        'total_area': 56.2,
        'living_area': 30.2,
        'kitchen_area': 8.5,
        'floors_total': 5
        }
]
BASE = "http://127.0.0.1:5000/"
# BASE = "http://151.248.122.251:5000/"
# response = requests.post(BASE + "predict", json=data)
response = requests.post(BASE + "predict", json=data_arr)

print(response.json())
