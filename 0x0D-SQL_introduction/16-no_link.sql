-- lists all records of a table
-- Don't list rows without name
-- Records should be listed in descending score
SELECT score, name FROM second_table WHERE name != ""
ORDER BY score DESC;
