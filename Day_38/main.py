import requests
from datetime import  datetime
import os


day=datetime.now()

nutrition_api=''
API_KEY=''
sheet_api = ''

APP_ID='1d3e68c9'
AGE=32
GENDER='FEMALE'
WEIGHT_KG=52
HEIGHT_CM=165
today = datetime.now().strftime('%d/%m/%Y')
now_time=datetime.now().strftime('%X')

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "age": AGE,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
}
 #https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise

response = requests.post(url=nutrition_api, json=parameters, headers=header)



results = {
    'day': day.strftime('%Y%m%d'),
    'input': response.json()['exercises'][0]['user_input'],
    'duration_min': response.json()['exercises'][0]['duration_min'],
    'calories': response.json()['exercises'][0]['nf_calories'],
 }
print(results)


sheet_inputs = {
    "workout": {
        "date": today,
        "time": now_time,
        "exercise": results["input"],
        "duration": results["duration_min"],
        "calories": results["calories"]
    }
}

sheet_response = requests.post(sheet_api, json=sheet_inputs)

print(sheet_response.text)
