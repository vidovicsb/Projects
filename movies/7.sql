SELECT title, rating FROM movies JOIN ratings ON movies.ID = ratings.movie_id WHERE year = 2010 ORDER BY rating DESC, title ASC;
