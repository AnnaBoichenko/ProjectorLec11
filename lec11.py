"""Create a program that allows you to search for images in gif format. The program 
should allow you to enter a search word. Using this word, search for GIFs using 
the Giphy API ([use their API](https://giphy.com/)). As a result, print the links to the
 GIFs."""


import requests


search_word = input("Enter a search word: ")
limit = input(f"How many gifs of '{search_word}' do you want to see? ")

my_api = "Oz3WcIC7oG1dCBZJSzV0og2uUgOtBlLi"
bare_url = "https://api.giphy.com/v1/gifs/search?"

parameters = {
    "api_key": my_api,
    "q": search_word,
    "limit": limit,
    "offset": 0,
    "rating": "g",
    "lang": "en",
    "bundle": "messaging_non_clips",
}

resp = requests.get(bare_url, params=parameters)

answer = []
for record in resp.json()["data"]:
    answer.append(record["url"])

print(*answer)
