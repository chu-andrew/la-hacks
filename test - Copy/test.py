from flask import Flask
from flask import request
from flask import render_template

import random

import yelp

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("my-form.html")  # This should be the name of your HTML file


@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['city']
    results = yelp.search_yelp("breakfast", text1)
    lunch_results = yelp.search_yelp("lunch", text1)
    dinner_results = yelp.search_yelp("dinner", text1)
    day_results = yelp.search_yelp(request.form['day'], text1)
    afternoon_results = yelp.search_yelp(request.form['afternoon'], text1)
    brunch = request.form.getlist("brunch")
    nights = request.form['nights']
    if len(results) == 0:
        return "No results found."
    else:
        out =  '''<style>body {
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
        out = f"{out} <h1>Your Itinerary for Your Trip to {text1}</h1>"
        for x in range(0, int(nights)+1):
            breakfast = results[random.randint(0, 9)]
            lunch = lunch_results[random.randint(0, 9)]
            dinner = dinner_results[random.randint(0, 9)]
            day = day_results[random.randint(0, 9)]
            afternoon = afternoon_results[random.randint(0, 9)]
            if len(brunch) > 0:
                out = f'''{out} <h2>Day {x+1}</h2><br />
                    You Will Visit: <a href="{day.url}" target=_blank>{day.name} --- {day.rating} STARS ({day.review_count})</a><br />
                    You Will Eat Brunch At: <a href="{lunch.url}" target=_blank>{lunch.name} --- {lunch.rating} STARS ({lunch.review_count})</a><br />
                    Then You Will Visit: <a href="{afternoon.url}" target=_blank>{afternoon.name} --- {afternoon.rating} STARS ({afternoon.review_count})</a><br />
                    You Will Eat Dinner At: <a href="{dinner.url}" target=_blank>{dinner.name} --- {dinner.rating} STARS ({dinner.review_count})</a><br />
                    <br />''' 
            else:
                out =  f'''{out} <h2>Day {x+1}</h2><br />
                    You Will Eat Breakfast At: <a href="{breakfast.url}" target=_blank>{breakfast.name} --- {breakfast.rating} STARS ({breakfast.review_count})</a><br />
                    Then You Will Visit: <a href="{day.url}" target=_blank>{day.name} --- {day.rating} STARS ({day.review_count})</a><br />
                    You Will Eat Lunch At: <a href="{lunch.url}" target=_blank>{lunch.name} --- {lunch.rating} STARS ({lunch.review_count})</a><br />
                    Then You Will Visit: <a href="{afternoon.url}" target=_blank>{afternoon.name} --- {afternoon.rating} STARS ({afternoon.review_count})</a><br />
                    You Will Eat Dinner At: <a href="{dinner.url}" target=_blank>{dinner.name} --- {dinner.rating} STARS ({dinner.review_count})</a><br />
                    <br />'''
            if int(nights)>0:
                out = f"{out} <p>You will be staying at hotel: <b>HOTEL</b></p>"
        out = f"{out} <a href='javascript:history.back()'>Return</a>"    
        return out

if __name__ == '__main__':
    app.run()