import os
import requests
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')
SHEETY_API_URL = os.getenv('SHEETY_API_URL')

exercise = input('Tell me which exercises you did: ')

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

body = {
    "query": exercise
}
response = requests.post(url=API_URL, headers=headers, json=body)
print(response.json())

exercise_data_raw = response.json()['exercises']

for exercise in exercise_data_raw:
    exercise_current = {
        "date": dt.datetime.now().strftime('%d/%m/%Y'),
        "time": dt.datetime.now().strftime('%H:%M:%S'),
        "exercise": exercise['name'].title(),
        "duration": exercise['duration_min'],
        "calories": exercise['nf_calories']
    }
    sheety_body = {
        "workout": exercise_current,
    }
    response_sheety = requests.post(url=SHEETY_API_URL, json=sheety_body)
    print(response_sheety.json())
