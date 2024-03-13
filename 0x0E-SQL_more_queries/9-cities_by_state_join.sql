-- 9-cities_by_state_join.sql

-- Query to list all cities along with their corresponding states using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
