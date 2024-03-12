-- Assuming the table dump has been imported into hbtn_0c_0 database

-- Calculate the average temperature during July and August by city and display the top 3 cities ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
