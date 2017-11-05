# coding: utf-8
#-------------------------------------------------------------------------------
# Name:        ohlc.py
# Purpose:
#
# Author:      Noah Huntington
#
# Created:     11/05/2017
# Copyright:   (c) Noah 2017
# Licence:     MIT
#-------------------------------------------------------------------------------

import pandas as pd
from datetime import datetime

import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:4KS5CJlz0ZX8Po@localhost:5432/postgres')


def main():
    
    #1M record test
    df = pd.read_sql_query("select * from merged ORDER BY timestamp limit 1000000;", engine)

    # use this in production instead
    #df = pd.read_sql_query("select * from merged;", engine)

    df = df.set_index(pd.DatetimeIndex(df['timestamp']))

    df.head()

    #5 MIN
    five_min_summary = pd.DataFrame()

    five_min_summary['open'] = df.groupby('symbol')["open"].resample("5T").first().ffill()
    five_min_summary['high'] = df.groupby('symbol')["high"].resample("5T").max().ffill()
    five_min_summary['low'] = df.groupby('symbol')["low"].resample("5T").min().ffill()
    five_min_summary['close'] = df.groupby('symbol')["close"].resample("5T").last().ffill()

    five_min_summary["interval"] = df.ix[4, 'interval'] = '5m'

    # five_min_summary.head()
    five_min_summary.to_sql('five_min_summary', engine, if_exists='replace')


    #15 MIN
    fifteen_min_summary = pd.DataFrame()

    fifteen_min_summary['open'] = df.groupby('symbol')["open"].resample("15T").first().ffill()
    fifteen_min_summary['high'] = df.groupby('symbol')["high"].resample("15T").max().ffill()
    fifteen_min_summary['low'] = df.groupby('symbol')["low"].resample("15T").min().ffill()
    fifteen_min_summary['close'] = df.groupby('symbol')["close"].resample("15T").last().ffill()

    fifteen_min_summary["interval"] = df.ix[4, 'interval'] = '15m'

    # fifteen_min_summary.head()
    fifteen_min_summary.to_sql('fifteen_min_summary', engine, if_exists='replace')


    #1HR
    hourly_summary = pd.DataFrame()

    hourly_summary['open'] = df.groupby('symbol')["open"].resample("H").first().ffill()
    hourly_summary['high'] = df.groupby('symbol')["high"].resample("H").max().ffill()
    hourly_summary['low'] = df.groupby('symbol')["low"].resample("H").min().ffill()
    hourly_summary['close'] = df.groupby('symbol')["close"].resample("H").last().ffill()

    hourly_summary["interval"] = df.ix[4, 'interval'] = '1H'

    # hourly_summary.head()
    hourly_summary.to_sql('hourly_summary', engine, if_exists='replace')


    #4HR
    four_hour_summary = pd.DataFrame()

    four_hour_summary['open'] = df.groupby('symbol')["open"].resample("4H").first().ffill()
    four_hour_summary['high'] = df.groupby('symbol')["high"].resample("4H").max().ffill()
    four_hour_summary['low'] = df.groupby('symbol')["low"].resample("4H").min().ffill()
    four_hour_summary['close'] = df.groupby('symbol')["close"].resample("4H").last().ffill()

    four_hour_summary["interval"] = df.ix[4, 'interval'] = '4H'

    # four_hour_summary.head()
    four_hour_summary.to_sql('four_hour_summary', engine, if_exists='replace')


    #1 Day
    daily_summary = pd.DataFrame()

    daily_summary['open'] = df.groupby('symbol')["open"].resample("D").first().ffill()
    daily_summary['high'] = df.groupby('symbol')["high"].resample("D").max().ffill()
    daily_summary['low'] = df.groupby('symbol')["low"].resample("D").min().ffill()
    daily_summary['close'] = df.groupby('symbol')["close"].resample("D").last().ffill()

    daily_summary["interval"] = df.ix[4, 'interval'] = '1D'

    # daily_summary.head()
    daily_summary.to_sql('daily_summary', engine, if_exists='replace')


    #1 Week
    weekly_summary = pd.DataFrame()

    weekly_summary['open'] = df.groupby('symbol')["open"].resample("W").first().ffill()
    weekly_summary['high'] = df.groupby('symbol')["high"].resample("W").max().ffill()
    weekly_summary['low'] = df.groupby('symbol')["low"].resample("W").min().ffill()
    weekly_summary['close'] = df.groupby('symbol')["close"].resample("W").last().ffill()

    weekly_summary["interval"] = df.ix[4, 'interval'] = '1W'

    # weekly_summary.head()
    weekly_summary.to_sql('weekly_summary', engine, if_exists='replace')


    #1 Month
    monthly_summary = pd.DataFrame()

    monthly_summary['open'] = df.groupby('symbol')["open"].resample("M").first().ffill()
    monthly_summary['high'] = df.groupby('symbol')["high"].resample("M").max().ffill()
    monthly_summary['low'] = df.groupby('symbol')["low"].resample("M").min().ffill()
    monthly_summary['close'] = df.groupby('symbol')["close"].resample("M").last().ffill()

    monthly_summary["interval"] = df.ix[4, 'interval'] = '1M'

    # monthly_summary.head()
    monthly_summary.to_sql('monthly_summary', engine, if_exists='replace')


    #1 Year
    yearly_summary = pd.DataFrame()

    yearly_summary['open'] = df.groupby('symbol')["open"].resample("AS").first().ffill()
    yearly_summary['high'] = df.groupby('symbol')["high"].resample("AS").max().ffill()
    yearly_summary['low'] = df.groupby('symbol')["low"].resample("AS").min().ffill()
    yearly_summary['close'] = df.groupby('symbol')["close"].resample("AS").last().ffill()

    yearly_summary["interval"] = df.ix[4, 'interval'] = '1Y'

    # yearly_summary.head()
    yearly_summary.to_sql('yearly_summary', engine, if_exists='replace')


if __name__ == '__main__':
    main()