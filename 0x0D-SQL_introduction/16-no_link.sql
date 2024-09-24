-- Script to list all records with non-empty name, displaying score and name

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
