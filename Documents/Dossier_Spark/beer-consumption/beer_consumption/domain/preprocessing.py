## 1. Which brewery produces the strongest beers by ABV%?
def meilleure_brasserie(data):
    max_abv =  data["beer_abv"].max()
    return data[data['beer_abv']==max_abv]["brewery_name"]

## 2. If you had to pick 3 beers to recommend using only this data, which would you pick ?