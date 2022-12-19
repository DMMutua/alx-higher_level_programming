-- Listing the number of records with the same `score` value.
-- Table: `second_table` 
-- Database: `hbtn_0c_0` [passed as a `mysql` argument]
-- List sorted in descending order, and display frequency.
SELECT score, COUNT('score') AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
