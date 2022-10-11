CREATE TABLE IF NOT EXISTS food(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    foodItem text NOT NULL,
    quantity integer NOT NULL,
    dateAdded text NOT NULL  
);