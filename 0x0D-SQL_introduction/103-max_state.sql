-- Assuming the table dump has been imported into hbtn_0c_0 database

-- Calculate the max temperature by state and display it ordered by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
