import json
import requests
import pandas as pd


def main():

    my_articles_dict = {}

    category = input("What are you looking for?: ")

    with open("config.json", "r") as j:
        config_json = json.load(j)
    
    #Extract
    query_params = {
        "category": category,
        "api_key": config_json["api_key"],

    }

    url = f'https://newsapi.org/v2/everything?q={query_params["category"]}&apiKey={query_params["api_key"]}'

    response = requests.request("GET", url)

    #Transform
    articles = response.json()['articles']

    for key in articles[0].keys():
        my_articles_dict[key] = []


    for key in my_articles_dict.keys():
        for article in articles:
            my_articles_dict[key].append(article[key])
            
        my_articles_dict[key] = pd.Series(my_articles_dict[key])

    article_data_frame = pd.DataFrame(my_articles_dict)

    #Load
    article_data_frame.to_excel(f'articulos_{category}.xlsx', sheet_name=category)

    print(article_data_frame.head())

if __name__ == '__main__':
    main()