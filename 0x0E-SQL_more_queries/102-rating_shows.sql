-- Select show titles and sum of ratings, ordering by rating sum in descending order
SELECT tv_shows.title, SUM(tv_shows_ratings.rate) AS rating_sum
FROM tv_shows
JOIN tv_shows_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
