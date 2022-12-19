-- Listing all records of `second_table` of database `hbtn_0c_0`-- Rows withut a `name` value are left out. 
-- Records listed by descending order.
-- database name will be passed as `mysql` argument
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
