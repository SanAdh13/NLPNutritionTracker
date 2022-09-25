import pandas as pd

'''just like the usda data this will take a sample of the positive yelp reviews
    An online annotation tool will be used to create the entity texts
    https://tecoholic.github.io/ner-annotator/

   this file will be run once, after fully completing usda set as it be same amount as usda set
    
'''

yelpLoc = "SpaCy/datasets/pos_reviews.csv"

def writeToFile(lines):
    with open("SpaCy/datasets/yelpDataToAnnotate.txt","w") as f:
        for x in lines:
            f.write(x)
            f.write('---')
        f.close()
def yelp():
    yelpDF = pd.read_csv(yelpLoc)
    yelpData = yelpDF.text
    yelpSample = yelpData.sample(n=30)

    writeToFile(yelpSample)
    

if __name__ == "__main__":
    yelp()