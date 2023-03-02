from flask import Flask, render_template
import random
import datetime
import requests

app =  Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0,10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    #rendering an element coming from python code -> Jinja {{}} in html
    # multiline {% for ....  %} {% endfor %}
    gender_url = f'https://api.genderize.io/?name={name}'
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', person_name=name, guess_gender=gender, guess_age=age)

@app.route('/blog')
def get_blog():
    blogs_url = 'https://www.npoint.io/docs/c790b4d5cab58020d391'
    blogs_response = requests.get(blogs_url)
    post_data = blogs_response.json()
    return render_template('blog.html', posts=post_data)


if __name__ == '__main__':
    app.run(debug=True)