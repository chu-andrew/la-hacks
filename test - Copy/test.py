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
        out = ""
        for x in range(0, int(nights)+1):
            breakfast = results[random.randint(0, 9)]
            lunch = lunch_results[random.randint(0, 9)]
            dinner = dinner_results[random.randint(0, 9)]
            day = day_results[random.randint(0, 9)]
            afternoon = afternoon_results[random.randint(0, 9)]
            if len(brunch) > 0:
                out = f'''{out} <h2>Day {x+1}</h2><br />
                    You Will Visit: {day.name} --- {day.rating} STARS ({day.review_count}) {day.url}<br />
                    You Will Eat Brunch At: {lunch.name} --- {lunch.rating} STARS ({lunch.review_count}) {lunch.url}<br />
                    Then You Will Visit: {afternoon.name} --- {afternoon.rating} STARS ({afternoon.review_count}) {afternoon.url}<br />
                    You Will Eat Dinner At: {dinner.name} --- {dinner.rating} STARS ({dinner.review_count}) {dinner.url}<br />
                    <br />''' 
            else:
                out =  f'''{out} <h2>Day {x+1}</h2><br />
                    You Will Eat Breakfast At: {breakfast.name} --- {breakfast.rating} STARS ({breakfast.review_count}) {breakfast.url}<br />
                    Then You Will Visit: {day.name} --- {day.rating} STARS ({day.review_count}) {day.url}<br />
                    You Will Eat Lunch At: {lunch.name} --- {lunch.rating} STARS ({lunch.review_count}) {lunch.url}<br />
                    Then You Will Visit: {afternoon.name} --- {afternoon.rating} STARS ({afternoon.review_count}) {afternoon.url}<br />
                    You Will Eat Dinner At: {dinner.name} --- {dinner.rating} STARS ({dinner.review_count}) {dinner.url}<br />
                    <br />'''
            if int(nights)>0:
                out = f"{out} <p>You will be staying at hotel: <b>HOTEL</b></p>"
        out = f"{out} <a href='javascript:history.back()'>Return</a>"    
        return out

if __name__ == '__main__':
    app.run()