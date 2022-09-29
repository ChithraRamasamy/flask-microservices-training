DROP TABLE IF EXISTS product;

CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT BETWEEN 20 and 300,
    price integer NOT NULL between 1 and 9999
    
    
);

