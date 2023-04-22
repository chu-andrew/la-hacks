from flask import Flask
from flask import request
from flask import render_template

from dataclasses import dataclass

import requests


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
    results = search_yelp("ice cream", text1)
    if len(results) == 0:
        return "No results found."
    else:
        out=""
        for location in results:
            out = f'{out} {location.name} --- {location.rating} STARS ({location.review_count} reviews)\n {location.url}'
        return out

if __name__ == '__main__':
    app.run()

from dataclasses import dataclass

import requests

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