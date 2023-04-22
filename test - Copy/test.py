from flask import Flask
from flask import request
from flask import render_template

from dataclasses import dataclass

import requests

import random


@dataclass
class YelpPlace:
    name: str
    rating: float
    review_count: int
    url: str


def search_yelp(query="Restaurants", city="Los Angeles, CA"):
    search_url = f"https://www.yelp.com/search/snippet?find_desc={query}&find_loc={city}&request_origin=user"
    search_response = requests.get(search_url)
    search_results = search_response.json()['searchPageProps']['mainContentComponentsListProps']

    yelp_results = []
    for result in search_results:
        if result['searchResultLayoutType'] == "iaResult":
            name = result['searchResultBusiness']['name']
            rating = result['searchResultBusiness']['rating']
            review_count = result['searchResultBusiness']['reviewCount']
            url = "https://www.yelp.com" + result['searchResultBusiness']['businessUrl']

            x = YelpPlace(
                name, rating, review_count, url
            )

            yelp_results.append(x)

    return yelp_results

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html") # This should be the name of your HTML file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['city']
    results = search_yelp("breakfast", text1)
    lunch_results = search_yelp("lunch", text1)
    dinner_results = search_yelp("dinner", text1)
    day_results = search_yelp(request.form['day'], text1)
    afternoon_results = search_yelp(request.form['afternoon'], text1)
    if len(results) == 0:
        return "No results found."
    else:
        breakfast = results[random.randint(0, 9)]
        lunch = lunch_results[random.randint(0, 9)]
        dinner = dinner_results[random.randint(0, 9)]
        day = day_results[random.randint(0, 9)]
        afternoon = afternoon_results[random.randint(0, 9)]
        return f'''You Will Eat Breakfast At: {breakfast.name} --- {breakfast.rating} STARS ({breakfast.review_count}) {breakfast.url}<br />
            Then You Will Visit: {day.name} --- {day.rating} STARS ({day.review_count}) {day.url}<br />
            You Will Eat Lunch At: {lunch.name} --- {lunch.rating} STARS ({lunch.review_count}) {lunch.url}<br />
            Then You Will Visit: {afternoon.name} --- {afternoon.rating} STARS ({afternoon.review_count}) {afternoon.url}<br />
            You Will Eat Dinner At: {dinner.name} --- {dinner.rating} STARS ({dinner.review_count}) {dinner.url}'''

if __name__ == '__main__':
    app.run()