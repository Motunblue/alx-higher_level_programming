-- lists the number of recoreds from same score in second_table
SELECT score, COUNT(*) as number FROM second_table GROUP by score
ORDER BY number DESC;
