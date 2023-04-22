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
    location = request.form['city']
    results = yelp.search_yelp("ice cream", location)
    if len(results) == 0:
        return "No results found."
    else:
        output = ""
        for location in results:
            line = f"<p>{location.name} --- {location.rating} STARS<p>"
            output += line
        return output


if __name__ == '__main__':
    app.run()
