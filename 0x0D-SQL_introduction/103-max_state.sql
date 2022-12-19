-- Displays maximum TEMP of each state
-- Ordering is done by State Name.

SELECT state, MAX(value) AS max_temp
FROM temperatures #0
GROUP BY state
ORDER BY state;
