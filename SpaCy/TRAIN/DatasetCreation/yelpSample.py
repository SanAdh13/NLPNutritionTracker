import pandas as pd

'''just like the usda data this will take a sample of the positive yelp reviews
    An online annotation tool will be used to create the entity texts
    https://tecoholic.github.io/ner-annotator/

   this file will be run once, after fully completing usda set as it be same amount as usda set
    
'''

#TODO: decrease some of the excessive whitespace in the yelp dataset


yelpLoc = "./datasets/pos_reviews.csv"

def writeToFile(lines):
    with open("datasets/yelpDataToAnnotate.txt","w") as f:
        for x in lines:

            #some of the data have too much whitespace; reducing it to one
            x = ' '.join(x.split())
            f.write(x)
            f.write('---') #adding as identifier for the annotator tool
        f.close()
def yelp():
    yelpDF = pd.read_csv(yelpLoc)
    yelpData = yelpDF.text
    yelpSample = yelpData.sample(n=50)

    writeToFile(yelpSample)
    

if __name__ == "__main__":
    yelp()