
# Installation - These are one time tasks

1) **Create** tables (sql/createTables.sql)
2) **COPY** (using psql cmd line) csvs to tables (sql/copyCSVs.sql)
3) **Insert** tables into one_minute master (sql/insertSymbols.sql)
4) **Drop** symbol tables (sql/dropSymbolTables.sql)


# Production - This is the script to be modified to adapt to the API
5) Run ohlc.py