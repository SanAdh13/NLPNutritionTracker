import pandas as pd;

# get the nutrition information from food.
#

location = "/datasets/___.csv"

def loadCSV():
    # this one create a dataframe for the csv
    # so we can use it throughtout this file 

    df = pd.read_csv(location)
    
    #TODO: some processing to have the relevant cols

    return df


def getFoodAndQuant(data):
    foods = []
    for d in data:
        foods.append([d[2],d[3]])
    return foods     
    

def getNutrition(data):

    csvDF = loadCSV()   #we load the nutrition csv
    # maybe after loading the CSV we just use the relevant cols to make the nutrition dict
    # we will have it as a dict 
    # key is the nutrition name: eg calories, fats 
    # value is the value of the nutrition : numerical data obv


    nutrition = {}

    userFoods = getFoodAndQuant(data) # we get only the food and quantity part from the db tuple passed from app.py
   

    for food,quant in userFoods:
        #TODO: find the food in the csv and fetch its nutrition

        #!important surround with try catch as some food may not be in the csv
        
        # after finding the item, need to do nutritionTotal = (per * quant) to get the total nutrition gain
        # increase the value of said nutrition in the dictionary 
        # we get the key and then do value += nutrtionTotal
        
        #eg key would be a column from the csv
        key = "cals"

        totalNutrition = 0
        #update the key in the value
        nutrition[key] = nutrition[key]+totalNutrition

    #TODO: we need to convert this dictionary into list of tuples
    # to follow the same format as the db. 
    # as we need to join them together to send in app.py
    return nutrition
    