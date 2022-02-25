import sqlite3

db = sqlite3.connect("src/database.db")

cur = db.cursor()

JSON = '{ "template-html.j2": [ "index.html", [ { "type": "column", "size": 1, "content": [ { "type": "row", "size": 1, "content": [ { "type": "scrolling horizontal", "content": { "type": "rss", "format": "${title} - ${description} - ", "length": 5, "url": "http://feeds.bbci.co.uk/news/rss.xml" }, "style": { "font-family": "Arial", "font-size": "30px", "color": "blue" }, "container_style": {}, "time": 0.5 } ] }, { "type": "row", "size": 1, "content": [ { "type": "scrolling vertical", "content": { "type": "text", "content": "This is some sample text to show on the screen." }, "style": { "font-family": "Arial", "font-size": "50px", "color": "blue" }, "container_style": { "background-image": "url(https://picsum.photos/800/600)", "background-repeat": "no-repeat", "background-size": "contain", "background-position": "center" }, "time": 0.5 } ] } ] }, { "type": "column", "size": 1, "content": [ { "type": "slideshow", "content": [ { "type": "image", "content": "https://picsum.photos/800/600", "time": 3000 }, { "type": "video", "content": "https://archive.org/download/electricsheep-flock-247-62500-7/00247%3D62517%3D62283%3D62016.mp4" }, { "type": "image", "content": "https://picsum.photos/800/600", "time": 3000 } ], "style": {}, "container_style": {} } ] }, { "type": "column", "size": 1, "content": [ { "type": "row", "size": 1, "content": [ { "type": "clock", "format": "${wday} ${date} ${mname} ${year}, ${h24}:${min}:${sec}", "style": { "font-family": "Arial", "font-size": "30px", "color": "blue" }, "container_style": {} } ] }, { "type": "row", "size": 1, "content": [ { "type": "video", "content": "https://www.w3schools.com/tags/movie.mp4", "style": {}, "container_style": { "background-color": "#d94ea4" } } ] } ] } ] ] }'

JSON2 = '''{
    "template-html.j2": [
        "index.html",
        [
            {
                "type": "row",
                "size": 9,
                "content": [
                    {
                        "type": "column",
                        "size": 2,
                        "content": [
                            {
                                "type": "row",
                                "size": 1,
                                "content": [
                                    {
                                        "type": "text",
                                        "style": {
                                            "font-size": "50px"
                                        },
                                        "content": {
                                            "type": "text",
                                            "content": "Sixth Form Notices"
                                        },
                                        "container_style": {}
                                    }
                                ]
                            },
                            {
                                "type": "row",
                                "size": 6,
                                "content": [
                                    {
                                        "type": "slideshow",
                                        "container_style": {},
                                        "content": [
                                            {
                                                "type": "image",
                                                "time": 5000,
                                                "content": "http://localhost:8080/media/image1.jpg"
                                            },
                                            {
                                                "type": "image",
                                                "time": 5000,
                                                "content": "http://localhost:8080/media/image2.jpg"
                                            },
                                            {
                                                "type": "image",
                                                "time": 5000,
                                                "content": "http://localhost:8080/media/image3.jpg"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "column",
                        "size": 1,
                        "content": [
                            {
                                "type": "row",
                                "size": 3,
                                "content": [
                                    {
                                        "type": "clock",
                                        "style": {
                                            "font-size": "60px",
                                            "color": "white"
                                        },
                                        "format": "${h24}:${min}",
                                        "container_style": {
                                            "background-color": "#4c0122"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "row",
                                "size": 1,
                                "content": [
                                    {
                                        "type": "text",
                                        "style": {
                                            "color": "white"
                                        },
                                        "content": {
                                            "type": "text",
                                            "content": "Upcoming Events"
                                        },
                                        "container_style": {
                                            "background-color": "#4c0122"
                                        }
                                    }
                                ]
                            },
                            {
                                "type": "row",
                                "size": 16,
                                "content": [
                                    {
                                        "type": "scrolling vertical",
                                        "style": {
                                            "color": "white",
                                            "font-size": "30px"
                                        },
                                        "time": 0.25,
                                        "content": {
                                            "type": "text",
                                            "content": "Wednesday 23rd Feb<br>Yr 13 Parents’ Evening<br><br>Thursday 24th Feb<br>Yr 13 Parents’ Evening<br><br>Thursday 3rd Mar<br>Non-uniform day for Dr Obote College<br><br>"
                                        },
                                        "container_style": {
                                            "background-color": "#4c0122"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "type": "row",
                "size": 1,
                "content": [
                    {
                        "type": "column",
                        "size": 1,
                        "content": [
                            {
                                "type": "text",
                                "style": {
                                    "font-size": "25pt",
                                    "color": "white"
                                },
                                "content": {
                                    "type": "text",
                                    "content": "News:"
                                },
                                "container_style": {
                                    "background-color": "#4c0122"
                                }
                            }
                        ]
                    },
                    {
                        "type": "column",
                        "size": 9,
                        "content": [
                            {
                                "type": "scrolling horizontal",
                                "content": {
                                    "type": "rss",
                                    "format": "${title} - ${description}  •  ",
                                    "length": 5,
                                    "url": "http://feeds.bbci.co.uk/news/rss.xml"
                                },
                                "time": 0.25,
                                "style": {
                                    "color": "white",
                                    "font-size": "25pt"
                                },
                                "container_style": {
                                    "background-color": "#4c0122"
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    ]
}'''

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

cur.execute("DELETE FROM content WHERE layout_ID = 2")
#cur.execute("INSERT INTO layouts VALUES (2, 'sixth-form', 1)")
cur.execute("INSERT INTO content VALUES (2, ?)", (JSON2, ))

db.commit()