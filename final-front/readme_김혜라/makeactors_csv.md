```python
import requests
import pandas


URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
'api_key': 'a019e211e4eb80411e10424e9f75bc1d',
'region': 'KR',
'language': 'ko',
}
response_movie = requests.get(URL + path, params=params)
result_movie = pandas.DataFrame(response_movie.json()['results'], columns=['id'])
a = pandas.DataFrame()
for i in result_movie.values:
    response_actor = requests.get(URL + f'/movie/{i[0]}/credits', params=params)
    result_actor = pandas.DataFrame(response_actor.json()['cast'], columns=['id'])
    if len(result_actor.values) >= 10:
        for ii in range(10):
            get_data = pandas.DataFrame({'movie_id': [i[0]], 'actor_id': [result_actor.values[ii][0]]})
            a = pandas.concat([a, get_data], ignore_index=True)
    else:
        for ii in range(len(result_actor.values)):
            get_data = pandas.DataFrame({'movie_id': [i[0]], 'actor_id': [result_actor.values[ii][0]]})
            a = pandas.concat([a, get_data], ignore_index=True)

    # for j in range(10):
    #     print(result_actor.values[j])
# a = pandas.DataFrame()
# for i in result.values:
#     for j in i[0]:
#         results = pandas.DataFrame({'movie_id': [i[1]], 'genre_id': [j]})
#         a = pandas.concat([a, results], ignore_index=True)

for iii in range(2, 101):
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': 'a019e211e4eb80411e10424e9f75bc1d',
    'region': 'KR',
    'language': 'ko',
    'page': iii
    }
    response_movie = requests.get(URL + path, params=params)
    result_movie = pandas.DataFrame(response_movie.json()['results'], columns=['id'])
    for i in result_movie.values:
        response_actor = requests.get(URL + f'/movie/{i[0]}/credits', params=params)
        result_actor = pandas.DataFrame(response_actor.json()['cast'], columns=['id'])
        if len(result_actor.values) >= 10:
            for ii in range(10):
                get_data = pandas.DataFrame({'movie_id': [i[0]], 'actor_id': [result_actor.values[ii][0]]})
                a = pandas.concat([a, get_data], ignore_index=True)
        else:
            for ii in range(len(result_actor.values)):
                get_data = pandas.DataFrame({'movie_id': [i[0]], 'actor_id': [result_actor.values[ii][0]]})
                a = pandas.concat([a, get_data], ignore_index=True)
    # response = requests.get(URL + path, params=params)
    # result2 = pandas.DataFrame(response.json()['results'], columns=['id', 'title','release_date', 'overview', 'poster_path', 'popularity', 'vote_average', 'vote_count'])
    # result = pandas.concat([result, result2], ignore_index=True)

    # for i in result.values:
    #     for j in i[0]:
    #         results = pandas.DataFrame({'movie_id': [i[1]], 'genre_id': [j]})
    #         a = pandas.concat([a, results], ignore_index=True)
a.to_csv('movie_actor.csv', encoding="utf-8-sig")
```

