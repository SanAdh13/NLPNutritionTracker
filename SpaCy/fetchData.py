import pandas as pd

locYelp = "SpaCy/datasets/pos_reviews.csv"
locUSDA = "SpaCy/datasets/food.csv"

def dataset():
   yelpDF = pd.read_csv(locYelp)
   usdaDF = pd.read_csv(locUSDA)
   ###########################USDA
   usdaDF = usdaDF.description
   

