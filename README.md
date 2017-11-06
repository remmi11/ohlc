
## Installation - These are one time tasks

1) **Create** tables (sql/createTables.sql)
2) **Copy** (using psql cmd line) csv's to tables (sql/copyCSVs.sql)
3) **Insert** tables into one_minute master (sql/insertSymbols.sql)
4) **Drop** individual symbol tables (sql/dropSymbolTables.sql)


## Production - This is the script to be modified to adapt to the API
5) Run scripts/ohlc.py