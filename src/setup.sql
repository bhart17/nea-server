CREATE TABLE users (
    user_ID INTEGER PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT);

CREATE TABLE layouts (
    layout_ID INTEGER PRIMARY KEY, 
    name TEXT UNIQUE, 
    owner_ID INTEGER);

CREATE TABLE content (
    layout_ID INTEGER UNIQUE, 
    data TEXT);