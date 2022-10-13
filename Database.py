import datetime
from locale import currency;
import sqlite3

from matplotlib import test;


# first we create an empty database file

def dbCheck():
    # the db is created automatically if it doesnt exist
    conn = sqlite3.connect('project.db')

    with open('schema.sql')as f:
        conn.executescript(f.read())

    return conn

def addToFoodTable(spacyResultArr):
    conn = dbCheck() #check db exist
    cur = conn.cursor() #create curson

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
            dataList.append([data]) #format: [date: result for that date]
            d = d - datetime.timedelta(days = 1)
        # print(dataList)
    
    elif(num == 3):
        startWeek = d - datetime.timedelta(days=d.weekday()) #get start of current week
        endofWeek = startWeek + datetime.timedelta(days=6) # gets end of current week
        for _ in range(num):    
            data = c.execute("select fooditem,quantity, dateAdded from food where dateAdded between ? and ?",(startWeek,endofWeek,)).fetchall()   
            # data = [tuple(row) for row in data]
            dataList.append(data)
            #go back a week, update the bounds to show start and end of that week 
            startWeek, endofWeek = startWeek - datetime.timedelta(days=7) , startWeek - datetime.timedelta(days=1)

    elif num == 2:
        for _ in range(num): 
            data = c.execute("select fooditem,quantity,dateAdded from food where strftime('%Y-%m',dateAdded) = ?",(d,) ).fetchall()
            # data = [tuple(row) for row in data]
            dataList.append(data)
            d = d.replace(month=d.month - 1 )
    conn.close()
    return dataList


def getFoodByDateRange(start,end ):
    conn = dbCheck()
    # conn.row_factory = sqlite3.Row
    conn.row_factory = lambda cursor, row : row[0:3]
    c = conn.cursor()
    data = c.execute('select fooditem, quantity,dateAdded from food where dateAdded between ? and ?',(start,end,)).fetchall()
    conn.close()
    # data = [tuple(row) for row in data]
    return data


# def test():
#     conn = dbCheck()
#     queries = [("apple","2","2021-07-10")
#             ,("oranges","2","2022-07-12")
#             ,("cherries","10","2022-07-22")
#             ,("chicken","200 g","2022-08-21")
#             ,("ribeye steak","300 g","2022-08-22")
#             ,("fried chicken wings","6","2022-09-13")
#             ,("burrito","1","2022-09-14")
#             ,("chips","1","2022-10-08")
#             ,("hamburger","2","2022-10-11")
#             ,("lamb chops","4","2022-10-13")
#             ,("chicken biryani","500 g","2022-10-13")
#             ,("naan bread","2","2022-10-13")]
#     cur = conn.cursor()
#     cur.executemany("Insert into food(foodItem,quantity,dateAdded) values(?,?,?)",queries )
#     conn.commit()
#     conn.close()
# def test2(d):
#     conn = dbCheck()
#     conn.row_factory = sqlite3.Row
#     data = conn.execute("select * from food WHERE strftime('%Y-%m', dateAdded) = ? ;",("2022-09",)).fetchall()
#     conn.close()
#     data = [tuple(row) for row in data]
#     return data



# if __name__ =="__main__":

    # # we get the current date
    # d = datetime.date.today()

    # conn = dbCheck()
    # print(conn.execute("select * from food where dateAdded = ?",(d,)).fetchall())

    # # this will get the start of the week
    # startWeek = d - datetime.timedelta(days=d.weekday())
    # #this will get the end of the week
    # endofWeek = startWeek + datetime.timedelta(days=6)
    # print( startWeek, endofWeek)
    # # for the last week we will just update 

    # startOfWeek, endofWeek = startWeek - datetime.timedelta(days=7) , startWeek - datetime.timedelta(days=1)


    # currMonth = str(d.year) +"-" +str(d.month)
    # print(d)

    # d = d.replace(month=d.month - 1 )
    
    # print(d)
   
    # prevWeek = startWeek - datetime.timedelta(days=7)
    # print(startWeek, prevWeek)
    # for i in range(5):
    #     print(d-datetime.timedelta(days=i))
    # x = getFood(5)
    
    # for v in range(len(x)):
    #     print(x[v][1])  