from flask import Flask
from flask import request
from flask import render_template

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