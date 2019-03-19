from flask import Flask, render_template
from random import randint

import requests
import json

app = Flask(__name__)


@app.route("/")
def movie_name():
    url = "https://api.themoviedb.org/3/movie/popular?api_key=919cb23948792d1ed26e74eb315c018e&language=en-US&page=1"

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    total_movies = parsed["results"]

    index_num = randint(0, len(total_movies))

    movie_name = parsed["results"][index_num]["title"]

    return render_template('index.html', movie_name=movie_name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
