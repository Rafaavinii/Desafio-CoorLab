from .models import Transport
import json


def convert(data):
    data = data.replace('R$ ', '').replace(',', '.')
    return float(data)

def load_data():
    try:
        with open('./data/data.json', 'r') as file:
            data = json.load(file)
        
        for transport in data['transport']:
            
            if not Transport.objects.filter(id = transport['id']).exists():
                Transport.objects.create(
                    id = transport['id'],
                    name = transport['name'],
                    price_confort = convert(transport['price_confort']),
                    price_econ = convert(transport['price_econ']),
                    city = transport['city'],
                    duration = int(transport['duration'].replace('h', '')),
                    seat = transport['seat'],
                    bed = transport['bed'],
                )

                print(f"{transport['name']} registered successfully")
            
            else:
                print(f"{transport['name']} already registered")

    except FileNotFoundError:
        return 'File not found'
