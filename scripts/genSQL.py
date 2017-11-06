#!/usr/bin/env python
#############################################################################
#title           :genSQL.py
#description     :This will create sql text to be executed in the sql window 
#                 for various tasks.
#author          :Noah Huntington
#date            :11/3/2017
#version         :0.1
#usage           :python genSQL.py
#notes           :
#python_version  :2.7.13
###############################################################################
import os

symbolList = ['AUDCAD',
'AUDJPY',
'AUDNZD',
'AUDUSD',
'CADJPY',
'EURAUD',
'EURCAD',
'EURGBP',
'EURJPY',
'EURNZD',
'EURUSD',
'GBPAUD',
'GBPCAD',
'GBPJPY',
'GBPNZD',
'GBPUSD',
'NZDCAD',
'NZDJPY',
'NZDUSD',
'USDCAD',
'USDJPY']

def selectFROM():
    
    f = open('sql/selectFROM.sql','w')

    for symbol in symbolList:

        f.write(
            """
            INSERT INTO one_minute
            SELECT * FROM {0};
            """ .format(symbol)
        )

    f.close()
    
# recursively generate create table statements for csv import
def create():
    
    f = open('sql/create.sql','w')

    for symbol in symbolList:

        f.write(
            """
                CREATE TABLE {0}
                (
                symbol text,
                d date,
                t time, 
                open numeric,
                high numeric,
                low numeric,
                closed numeric
                );
            """ .format(symbol)
        )

    f.close()


# recursively generate csv copy statements
def insertSQL():
    
    f = open('sql/insert.sql','w')

    for symbol in symbolList:
        f.write(
            """
            COPY {0} (symbol, d, t, open, high, low, closed) FROM 'C:/Users/wtgeo_000/Desktop/ohlc/1min/{1}' CSV HEADER DELIMITER ',';
            """ .format(symbol)
        )

    f.close()


# recursively generate insert from table statements for merging currency tables
def mergeSQL():
    f = open('sql/merge.sql','w')

    for symbol in symbolList:
        f.write(
        """
            INSERT INTO one_minute (Symbol, Timestamp, Open, High, Low, Close) SELECT Symbol, Timestamp, Open, High, Low, Close FROM {0};
        """ .format(symbol)
        )

    f.close()


# drop all currency tables
def drop():
    
    f = open('sql/drop.sql','w')

    for file in os.listdir("1min"):

        f.write(
            """
                DROP TABLE {0};

            """ .format(file[:-4])
        )

    f.close()
        

selectFROM()
# create()
# insertSQL()
#mergeSQL()
# drop()