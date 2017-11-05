DROP TABLE test;
DROP TABLE test2;
SELECT * into test2 FROM merged LIMIT 1000000; 

SELECT 
symbol,
open,
high,
low,
closed,
(d || ' ' || t) AS timestamp
into test
FROM test2;


ALTER TABLE test ADD COLUMN interval character varying(10)
ALTER TABLE test RENAME COLUMN closed TO close;
SELECT * FROM "5m_test";