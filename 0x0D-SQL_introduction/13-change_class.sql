-- Removing all records with a `score` <= 5 in `second_table`
-- the database name `hbtn_0c_0` will be passed as an argument
-- 	of the `mysql` command.
DELETE FROM second_table
WHERE score <= 5;
