## 1. Which brewery produces the strongest beers by ABV%?

def meilleure_brasserie(data):
    max_abv =  data["beer_abv"].max()
    return data[data['beer_abv']==max_abv]["brewery_name"]