DROP TABLE test;
--DROP TABLE test2;
SELECT * into test2 FROM merged LIMIT 100000; 

SELECT 
symbol,
open,
high,
low,
close,
(d || ' ' || t) AS timestamp
into test
FROM test2;

ALTER TABLE test ADD COLUMN interval character varying(10);

ALTER TABLE test RENAME COLUMN closed TO close;

ALTER TABLE test RENAME TO one_minute;

select * from (
  SELECT "timestamp",
  ROW_NUMBER() OVER(PARTITION BY symbol, "timestamp" ORDER BY "timestamp" asc) AS Row
  FROM one_minute
) dups
where 
dups.Row > 1