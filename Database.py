import datetime

import sqlite3

import re;


# first we create an empty database file

def dbCheck():
    # the db is created automatically if it doesnt exist
    conn = sqlite3.connect('project.db')
    with open('schema.sql')as f:
        conn.executescript(f.read())
    return conn

def addToFoodTable(spacyResultArr):
    conn = dbCheck() #check db exist
    cur = conn.cursor() #create cursor
    date = datetime.date.today() #get todays date 
    query = "INSERT INTO food(foodItem,quantity,dateAdded) values (?,?,?);" 
    for values in spacyResultArr: #the list we get from the spacy NER we add each element to the db 
        #values; [0] is the food [1] is its quantity
        cur.execute(query,(values[0],values[1],date))
    conn.commit()
    cur.close()
    conn.close()

def getFood(num):
    conn = dbCheck()
    # conn.row_factory = sqlite3.Row
    conn.row_factory = lambda cursor, row : row[0:3]
    c = conn.cursor()
    d = datetime.date.today() 

    dataList = []
    if(num == 5):
        #this one is for the last 5 day 
        for _ in range(num):
            data = c.execute("select fooditem,quantity,dateAdded from food where dateAdded = ?",(d,)).fetchall()
            # data = [tuple(row) for row in data]
            nutrition = getNutrition(data)

            ylabel = str(d.year)+"-"+str(d.month)+"-"+str(d.day)

            dataList.append((data,nutrition,ylabel))
            d = d - datetime.timedelta(days = 1)
    elif(num == 3):
        startWeek = d - datetime.timedelta(days=d.weekday()) #get start of current week
        endofWeek = startWeek + datetime.timedelta(days=6) # gets end of current week
        for _ in range(num):    
            data = c.execute("select fooditem,quantity, dateAdded from food where dateAdded between ? and ?",(startWeek,endofWeek,)).fetchall()   
            #IF i pass the data here and then i can append that arraylist to the end
            nutrition = getNutrition(data)

            date = str(startWeek)+" to "+str(endofWeek)
            dataList.append((data,nutrition,date))
            #go back a week, update the bounds to show start and end of that week 
            startWeek, endofWeek = startWeek - datetime.timedelta(days=7) , startWeek - datetime.timedelta(days=1)

    elif(num == 2):
        d = datetime.date.today() 
        # d = 
        for _ in range(num): 
            month = str(d.year)+"-"+"%02d"%d.month
            # dateMonth=(str(d.year)+"-"+str(d.month))
            data = c.execute('select fooditem,quantity,dateAdded from food where strftime("%Y-%m",dateAdded) = ?',(month,)).fetchall()
            # data = c.execute("select fooditem,quantity,dateAdded from food where strftime('%Y-%m',dateAdded) = ?",(d,) ).fetchall()
            nutrition = getNutrition(data)
            # dateMonth=(str(d.year)+"-"+str(d.month))
            dataList.append((data,nutrition,month))
            d = d.replace(month=d.month - 1 )
    conn.close()
    return dataList


def getFoodByDateRange(start,end ):

    #Same as get daily select option but this is for the selected amount of days 
    conn = dbCheck()
    conn.row_factory = lambda cursor, row : row[0:3]
    c = conn.cursor()
    dataList= []    
    noOfDays = (end - start).days
    for _ in range(noOfDays+1):
        data = c.execute("select fooditem,quantity,dateAdded from food where dateAdded = ?",(start,)).fetchall()
        nutrition = getNutrition(data)
        ylabel = str(start.year)+"-"+str(start.month)+"-"+str(start.day)
        dataList.append((data,nutrition,ylabel))
        start = start + datetime.timedelta(days = 1)
    conn.close()
    return dataList



def createQuery(food):
    query = "select * from nutrition where "
    if len(food) == 1:
        query+= '"Food Name" like "%'+food[0] + '%"'
    else: 
        for i in range(len(food)):
            if(i != len(food)-1):
                query+= '"Food Name" like "%'+food[i] +'%" and '
            else:
                query+= '"Food Name" like "%'+food[i]+'%"'

    return query

def getNutrition(data):
    conn = dbCheck()

    # the data that is passed is all the food items for that select timeframe T 
    # when the user picks one of the select options, the data is returned as array with n timeframes 
    # each T has n amounts of food records F
    # each F = [food,quantity,dateAdded ] 

    #this will keep the nutrition total for the timeframe
    # each index corresponds to one of the nutrient in the DB
    nutritionArray = [0 for _ in range(9)]
    for foodrecord in data:  
        food, quantity = foodrecord[0],foodrecord[1]
        try:
            if not (quantity.isnumeric()):
                quantity = re.findall(r'\b\d+\b', quantity)
                quantity = (float(quantity[0])/100)
        except:
            pass

        #if the food is a multi worded food we split it for the db 
        food = food.lower().split()
        #
        query = createQuery(food)

        nutriData = conn.execute(query).fetchall()   
        try:
            nutriData = nutriData[0]
            values = nutriData[2:]
            for i in range(9):
                nutritionArray[i]+=(float(values[i]) * float(quantity))  
        except:
            pass

    return nutritionArray

# def test(x):
#     conn = dbCheck()
#     conn.row_factory = lambda cursor, row : row[0:3]
#     c = conn.cursor()

#     d= datetime.date.today()

#     data = c.execute('select fooditem,quantity,dateAdded from food where strftime("%Y-%m",dateAdded) = ?',(x,)).fetchall()
#             # data = [tuple(row) for row in data]
#     print(data)
#             #IF i pass the data here and then i can append that arraylist to the end
    

        


# if __name__ == "__main__":

    # date = "2022-09-09"
    # format = "%Y-%m-%d"
    # date = datetime.datetime.strptime(date,format)

    # # print(date)

    # # d = datetime.date.today()
    # month = str(date.year)+"-"+"%02d" %date.month
    # print(month)

    # print(month)
    # print(date.strftime("%Y-%m-%d"))
    # print(test(month))

    # print(getFood(2))


 