-- Selecting show titles and their corresponding total rating
SELECT tv_shows.title, SUM(rating) rating
FROM tv_shows
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
