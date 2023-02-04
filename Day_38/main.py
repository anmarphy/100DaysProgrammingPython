import requests
from datetime import  datetime

day=datetime.now()

nutrition_api='https://trackapi.nutritionix.com/v2/natural/exercise'
API_KEY='c2551f419b48340650abeee76c92dd1d'
APP_ID='1d3e68c9'
AGE=32
GENDER='FEMALE'
WEIGHT_KG=52
HEIGHT_CM=165


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
    'day':day.strftime('%Y%m%d'),
    'input': response.json()['exercises'][0]['user_input'],
    'duration_min': response.json()['exercises'][0]['duration_min'],
    'calories': response.json()['exercises'][0]['nf_calories'],
 }
print(results)