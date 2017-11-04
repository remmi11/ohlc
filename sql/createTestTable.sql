DROP TABLE IF exists test;

select *,
d::date + t::interval AS timestamp
into test
from merged  
LIMIT 20000; 