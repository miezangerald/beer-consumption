## 1. Which brewery produces the strongest beers by ABV%?
def meilleure_brasserie(data):
    max_abv =  data["beer_abv"].max()
    return data[data['beer_abv']==max_abv]["brewery_name"]


## 2. If you had to pick 3 beers to recommend using only this data, which would you pick ?

# convertir en date
from datetime import datetime
def converTime(entier):
    date =  datetime.fromtimestamp(entier)
    return date.strftime('%d/%m/%Y')

# creer la variable date
def biere_date(df):
    df['date'] =  df['review_time'].apply(lambda x: converTime(x))
    return df

# creer la variable annee
def biere_annee(df):
    df["annee"] = df['date'].apply(lambda x: x.split("/")[2])
    df["annee"] = df["annee"].astype(int)
    return df

# les bieres selectionnees apres la date max
def beer_review_after_max_date(df):
    mask = df['annee'] >= df['annee'].max()
    return df[mask]

## 3. Which of the factors (aroma, Tate, appearance, palate) are most important in determining the overall quality of a beer ?
