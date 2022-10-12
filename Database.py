import datetime;
import sqlite3;


# first we create an empty database file

def dbCheck():
    # the db is created automatically if it doesnt exist
    conn = sqlite3.connect('project.db')

    with open('schema.sql')as f:
        conn.executescript(f.read())

    return conn

def addToFoodTable(spacyResultArr):

    #firstly we will check if the db exists 
    conn = dbCheck() 
    cur = conn.cursor()

    # now we want to make a connection to the db to add to the table 
    
    ##the array is currenlty in the format 
    # food | quantity
    # 
    # we want to save it in database in the format
    # food | quantity | date   

    date = datetime.datetime.now()
    query = "INSERT INTO food(foodItem,quantity,dateAdded) values (?,?,?);"

    for values in spacyResultArr:
        #values; [0] is the food [1] is the quantity
        cur.execute(query,(values[0],values[1],date))

    conn.commit()
    cur.close()
    conn.close()


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
Statements = [
    'select * from food'
    'select * from food, grouped by #TODO: day',
    'select * from food, grouped by #TODO: week',
    'select * from food, grouped by #TODO: month',
    'select * from food, grouped by #TODO: year']

def getFood(num):
    conn = dbCheck()
    conn.row_factory = sqlite3.Row
    data = conn.execute(Statements[num]).fetchall()
    conn.close()
    data = [tuple(row) for row in data]
    return data


def getFoodByDateRange(start,end ):
    conn = dbCheck()
    conn.row_factory = sqlite3.Row
    data = conn.execute('select * from food where dateAdded between ? and ?',(start,end,)).fetchall()
    conn.close()
    data = [tuple(row) for row in data]
    return data



# def getFoodByDay():
#     conn = dbCheck()
#     conn.row_factory = sqlite3.Row
#     data = conn.execute('select * from food, grouped by ').fetchall()
#     conn.close()
#     return data

# def getFoodByWeek():
#     conn = dbCheck()
#     conn.row_factory = sqlite3.Row
#     data = conn.execute('select * from food, grouped by ').fetchall()
#     conn.close()
#     return data

# def getFoodByMonth():
#     conn = dbCheck()
#     conn.row_factory = sqlite3.Row
#     data = conn.execute('select * from food, grouped by ').fetchall()
#     conn.close()
#     return data

# def getFoodByYear():
#     conn = dbCheck()
#     conn.row_factory = sqlite3.Row
#     data = conn.execute('select * from food, grouped by ').fetchall()
#     conn.close()
#     return data






    

