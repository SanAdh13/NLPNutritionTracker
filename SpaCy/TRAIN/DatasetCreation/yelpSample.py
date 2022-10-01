import pandas as pd

'''just like the usda data this will take a sample of the positive yelp reviews
    An online annotation tool will be used to create the entity texts
    https://tecoholic.github.io/ner-annotator/
'''

yelpLoc = "./datasets/csv/pos_reviews.csv"

def writeToFile(lines):
    with open("./datasets/yelpDataToAnnotate.txt","w") as f:
        for x in lines:

            #some of the data have too much whitespace; reducing it to one
            x = ' '.join(x.split())
            f.write(x)
            f.write('---') #adding as identifier for the annotator tool
        f.close()

def yelp():
    yelpDF = pd.read_csv(yelpLoc)
    yelpData = yelpDF.text
    yelpSample = yelpData.sample(n=200)
    writeToFile(yelpSample)
    
if __name__ == "__main__":
    yelp()