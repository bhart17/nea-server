import sqlite3

db = sqlite3.connect("src/database.db")

cur = db.cursor()

JSON = str(
    '{ "template-html.j2": [ "index.html", [ { "type": "column", "size": 1, "content": [ { "type": "row", "size": 1, "content": [ { "type": "scrolling horizontal", "content": { "type": "rss", "format": "${title} - ${description} - ", "length": 5, "url": "http://feeds.bbci.co.uk/news/rss.xml" }, "style": { "font-family": "Arial", "font-size": "30px", "color": "blue" }, "container_style": {}, "time": 0.5 } ] }, { "type": "row", "size": 1, "content": [ { "type": "scrolling vertical", "content": { "type": "text", "content": "This is some sample text to show on the screen." }, "style": { "font-family": "Arial", "font-size": "50px", "color": "blue" }, "container_style": { "background-image": "url(https://picsum.photos/800/600)", "background-repeat": "no-repeat", "background-size": "contain", "background-position": "center" }, "time": 0.5 } ] } ] }, { "type": "column", "size": 1, "content": [ { "type": "slideshow", "content": [ { "type": "image", "content": "https://picsum.photos/800/600", "time": 3000 }, { "type": "video", "content": "https://archive.org/download/electricsheep-flock-247-62500-7/00247%3D62517%3D62283%3D62016.mp4" }, { "type": "image", "content": "https://picsum.photos/800/600", "time": 3000 } ], "style": {}, "container_style": {} } ] }, { "type": "column", "size": 1, "content": [ { "type": "row", "size": 1, "content": [ { "type": "clock", "format": "${wday} ${date} ${mname} ${year}, ${h24}:${min}:${sec}", "style": { "font-family": "Arial", "font-size": "30px", "color": "blue" }, "container_style": {} } ] }, { "type": "row", "size": 1, "content": [ { "type": "video", "content": "https://www.w3schools.com/tags/movie.mp4", "style": {}, "container_style": { "background-color": "#d94ea4" } } ] } ] } ] ] }'
)

# cur.execute(
#     "CREATE TABLE users (user_ID INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)"
# )
# cur.execute(
#     "CREATE TABLE layouts (layout_ID INTEGER PRIMARY KEY, name TEXT UNIQUE, owner_ID INTEGER)"
# )
# cur.execute("CREATE TABLE content (layout_ID INTEGER UNIQUE, data TEXT)")

#cur.execute("INSERT INTO layouts VALUES (1, 'test', 1)")
# cur.execute("DELETE FROM users")
# cur.execute(
#     "INSERT INTO users VALUES (1, 'bob', '$2b$12$qkZCT9kG8Llw2ON0BlgROeFvJkWM.jRMGqgilypK1JAaljkGetiX.')"
# )

cur.execute("DELETE FROM content")
cur.execute("INSERT INTO content VALUES (1, ?)", (JSON, ))

db.commit()