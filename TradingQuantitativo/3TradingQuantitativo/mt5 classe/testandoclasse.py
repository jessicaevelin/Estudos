from mt5_classe import AsimoTrader
import pandas as pd
from datetime import date, datetime
import os

file_path = '3TradingQuantitativo\mt5 classe\pass.txt'

trader = AsimoTrader(file_path)

trader.update_ohlc(symbol='PETR4', timeframe = TIMEFRAME_D1)

df  = trader.read_ohlc(symbol='PETR4', timeframe = TIMEFRAME_D1, initial_date =datetime(2019,1,1))

df.head()
