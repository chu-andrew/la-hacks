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

    hotel_search = yelp.search_yelp("hotels", location)

    out = '''<style>body {
            background-color: black;
            font-family: Verdana;
            font-size: 1.25rem;
            color: rebeccapurple;
            padding-left: 200px;
        }
        h1 {
            font-family: Arial Narrow;
            color: rebeccapurple;
            font-stretch: condensed;
            font-weight: bold;
            font-size: 7rem;
        }
        h3 {
            font-family: Arial;
            color: saddlebrown;
        }
        p {
            font-family: Times New Roman;
            color: lightgrey;
            font-size: 0.75rem;
        }
        #submit {
            background: mediumpurple;
            color: white;
            border-style: outset;
            border-color: darkgrey;
            height: 50px;
            width: 200px;
            font: bold15px arial;
            text-shadow: none;

        }
        #select {
            background-color: lightgrey;
            font-family: Georgia;
        }
        a:visited, a:active, a:link {
            text-decoration: none;
            color: purple;
        }
        a:hover {
            color: hotpink;
        }</style>'''

    out = f"{out} <h1>{location.lower()}</h1>"

    for x in range(0, int(nights) + 1):
        breakfast = breakfast_search[random.randint(0, 9)]
        lunch = lunch_search[random.randint(0, 9)]
        dinner = dinner_search[random.randint(0, 9)]
        day = day_search[random.randint(0, 9)]
        afternoon = afternoon_search[random.randint(0, 9)]
        hotel = hotel_search[random.randint(0,9)]

        if len(brunch) > 0:
            out = f'''{out} <h2>Day {x + 1}</h2><br />
                A Trip to {info_string(day)}<br />
                Brunch at {info_string(lunch)}<br />
                A Visit to {info_string(afternoon)}<br />
                Dinner at {info_string(dinner)}<br />
                <br />'''
        else:
            out = f'''{out} <h2>Day {x + 1}</h2><br />
                Breakfast at {info_string(breakfast)}<br />
                A Trip to {info_string(day)}<br />
                Lunch at {info_string(lunch)}<br />
                A Visit to {info_string(afternoon)}<br />
                Dinner at {info_string(dinner)}<br />
                <br />'''
        if int(nights) > 0:
            out = f"{out} <p>Rest and relaxation at {info_string(hotel)}</p>"
    out = f"{out} <a href='javascript:history.back()'>Return</a>"
    return out


if __name__ == '__main__':
    app.run()
