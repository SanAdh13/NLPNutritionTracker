import datetime;
import sqlite3;


"""
this function will be used to create the sqlite DB 
"""
def createDB():
    
    return 0

"""
    A table for the food stuff to add for the user 
    eg. 
    DATE    | FOODTYPE  | FOODITEM | QUANTITY
    12-2-22 | Breakfast | Eggs     | 2
"""
def addToFoodTable(foodType,foodItem,quantity):   

    date = datetime.date.today()
    
    #add to sql table
    


"""
    We will need to fetch the food data by the date

    something like will have to test out
    select all from foodTable groupBy Foodtype, Date  

    ideally we want to show back to the user the nutrition information
    in these formats in the page:
        pie chart: 3 sections showing calories spread for each meal B/L/D
        table: the actual nutrition breakdown for all food item 
            eg. total calorie intake, protein, fats (saturates and unsaturated) etc
        some other charts should be observed aswell just to see
"""    
def getFood(date):
    return 0    

