from flask import Flask
from flask import request
from flask import render_template

import random

import yelp


def info_string(place):
    return f"<a href = '{place.url}' target=_blank > {place.name} ({place.rating}★)</a>"


app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("itinerary_form.html")  # This should be the name of your HTML file


@app.route('/', methods=['POST'])
def my_form_post():
    location = request.form['city']

    breakfast_search = yelp.search_yelp("breakfast", location)
    lunch_search = yelp.search_yelp("lunch", location)
    dinner_search = yelp.search_yelp("dinner", location)

    day_search = yelp.search_yelp(request.form['day'], location)
    afternoon_search = yelp.search_yelp(request.form['afternoon'], location)

    brunch = request.form.getlist("brunch")
    nights = request.form['nights']

    out = '''<style>body {
                    background-color: sand;
                    background-image: url("https://th.bing.com/th/id/OIP.Ihlflmu84jNLfnYgr4E8cQHaFJ?w=219&h=180&c=7&r=0&o=5&dpr=1.4&pid=1.7");
                    background-size: 150px 200px;
                    font-family: Verdana;
                    font-weight: bold;
                    font-style: italic;
                    font-size: 1.25rem;
                    color: rebeccapurple;
                    padding-left: 200px;
                }
                h1 {
                    font-family: Georgia;
                    color: darkred;
                }
                h3 {
                    font-family: Arial;
                    color: saddlebrown;
                }
                p {
                    font-family: Times New Roman;
                    color: black;
                    font-size: 0.75rem;
                }</style>'''

    out = f"{out} <h1>Your Itinerary for Your Trip to {location}</h1>"

    for x in range(0, int(nights) + 1):
        breakfast = breakfast_search[random.randint(0, 9)]
        lunch = lunch_search[random.randint(0, 9)]
        dinner = dinner_search[random.randint(0, 9)]
        day = day_search[random.randint(0, 9)]
        afternoon = afternoon_search[random.randint(0, 9)]

        if len(brunch) > 0:
            out = f'''{out} <h2>Day {x + 1}</h2><br />
                A Trip to {info_string(day)}<br />
                Lunch at {info_string(lunch)}<br />
                A Visit to {info_string(afternoon)}<br />
                Dinner at: {info_string(dinner)}<br />
                <br />'''
        else:
            out = f'''{out} <h2>Day {x + 1}</h2><br />
                Breakfast at {info_string(breakfast)}<br />
                A Trip to {info_string(day)}<br />
                Lunch at {info_string(lunch)}<br />
                A Visit to {info_string(afternoon)}<br />
                Dinner at: {info_string(dinner)}<br />
                <br />'''
        if int(nights) > 0:
            out = f"{out} <p>You will be staying at hotel: <b>HOTEL</b></p>"
    out = f"{out} <a href='javascript:history.back()'>Return</a>"
    return out


if __name__ == '__main__':
    app.run()
