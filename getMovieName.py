# import requests
# import json
#
# from random import randint
#
# url = "https://api.themoviedb.org/3/movie/popular?api_key=919cb23948792d1ed26e74eb315c018e&language=en-US&page=1"
#
# response = requests.get(url)
# data = response.text
# parsed = json.loads(data)
#
# totalMovies = parsed["results"]
#
# index_num = randint(0, len(totalMovies))
#
# movie_name = parsed["results"][index_num]["original_title"]
#
# print(movie_name)
#
