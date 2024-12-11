from cs50 import SQL

db = SQL("sqlite:///favorites.db")

list = ["Adventure Time",
        "Arrow",
        "Avatar: The Last Airbender",
        "Brooklyn Nine-Nine",
        "Community",
        "Family Guy",
        "Friends",
        "Game of Thrones",
        "Gilmore Girls",
        "Grey’s Anatomy",
        "How I Met Your Mother",
        "It’s Always Sunny in Philadelphia",
        "Parks and Recreation",
        "Sherlock",
        "Squid Game",
        "The Bachelorette",
        "The Crown",
        "The Office",
        "The Queen’s Gambit",
        "The Untamed"]

for i in list:
    rows = db.execute("SELECT title FROM shows WHERE title LIKE ?", i)
    print(rows[1])
