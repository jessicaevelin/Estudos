import MetaTrader5 as mt5
import json
import MetaTrader5 as mt5
from datetime import datetime, timedelta
import pandas as pd
import os

class AsimoTrader():
    def __init__(self, file_path=None, Login=None, password=None, server=None):
        if file_path:
            try:
                with open(file_path) as f:
                    credentials = json.load(f)
                    
                self.login = credentials['Login']
                self.password = credentials['password']
                self.server = credentials['server']
                
            except: print('Erro ao ler as credentiais'); quit()
        
        else:
                self.login = Login
                self.password = password
                self.server = server
                if (Login and password and server) == None:
                    print('Erro ao ler as credenciais'); quit()
                    
        if not mt5.initialize(Login=self.login, password=self.password, server=self.server):
            #print(mt5.last_error())
            mt5.shutdown()
            quit()
        
        self.timeframe_dict = {
            'TIMEFRAME_M1' : [mt5.TIMEFRAME_M1, 60],
            'TIMEFRAME_M2' : [mt5.TIMEFRAME_M2, 120],
            'TIMEFRAME_M3' : [mt5.TIMEFRAME_M3, 180],
            'TIMEFRAME_M4' : [mt5.TIMEFRAME_M4, 240],
            'TIMEFRAME_M5' : [mt5.TIMEFRAME_M5, 300],
            'TIMEFRAME_M6' : [mt5.TIMEFRAME_M6, 360],
            'TIMEFRAME_H1' : [mt5.TIMEFRAME_H1, 3600],
            'TIMEFRAME_D1' : [mt5.TIMEFRAME_D1, 86400],
            'TIMEFRAME_W1' : [mt5.TIMEFRAME_W1, 604800],
            'TIMEFRAME_MN1' : [mt5.TIMEFRAME_MN1, 2592000]
        }
        
        if not os.path.isdir('ohlc'):
            os.mkdir('ohlc')
            for timeframe in self.timeframe_dict.keys():
                try:
                    os.mkdir(f'ohlc\\{timeframe}')
                except FileExistsError: pass
        elif not os.path.isdir('ticks'):
            os.mkdir('ticks')
            
        # Funções
        
        def update_ohlc(self, symbol, timeframe):
            initial_date = datetime(2012,1,1)
            final_date = datetime.now()
            
            if not os.path.exists(f'ohlc\\{timeframe}\\{symbol}_{timeframe}.csv'):
                df = pd.DataFrame(columns = ['time', 'open', 'high','low', 'close', 'tick_volume', 'spread', 'real_volume'])
                
            else:
                df = pd.read_csv(f'ohlc\\{timeframe}\\{symbol}_{timeframe}.csv')
                df['time'] = pd.to_datetime(df['time'], unit='s')
                if df['time'].max() < datetime.now() - timedelta(days=7):
                    initial_date = df['time'].max()
                else:
                    return
        
            timedelta_default = timedelta(days=self.timeframe_dict[timeframe][1])
            final_date_aux = initial_date + timedelta_default
            timeframe_name = timeframe
            timeframe = self.timeframe_dict[timeframe][0]
            
            while True:
                data_aux = mt5.copy_rates_ranges(symbol, timeframe, initial_date, min(final_date_aux, final_date))
                df_aux = pd.DataFrame(data_aux)
                df_aux['time'] = pd.to_datetime(df_aux['time'], unit='s')
                df = pd.concat([df_aux, df] , ignore_index=True)
                
                if final_date_aux > final_date: break
                
                initial_date = df_aux['time'].max()
                final_date_aux = initial_date + timedelta_default
                
            df.sort_values(by='time', ascending=False, inplace = True)
            df.to_csv(f'ohlc\\{timeframe}\\{symbol}_{timeframe}.csv', index=False)
                
            
            def update_ticks(self, symbol):
                initial_date = datetime(2012,1,1)
                final_date = datetime.now()
                
                if not os.path.exists(f'ticks\\{timeframe}\\{symbol}_ticksrange.csv'):
                    df = pd.DataFrame(columns = ['time', 'open', 'high','low', 'close', 'tick_volume', 'spread', 'volume_real'])
                    
                else:
                    df = pd.read_csv(f'ticks\\{timeframe}\\{symbol}_ticksrange.csv')
                    df['time'] = pd.to_datetime(df['time'], unit='s')
                    if df['time'].max() < datetime.now() - timedelta(days=7):
                        initial_date = df['time'].max()
                
                ticks_data = mt5.copy_ticks_range(symbol, initial_date, final_date, mt5.COPY_TICKS_TRADE)
                df_aux = pd.DataFrame(ticks_data)
                df_aux['time'] = pd.to_datetime(df_aux['time'], unit='s')
                df = pd.concat([df_aux, df] , ignore_index=True)
                df_aux['time'] = pd.to_datetime(df_aux['time'])

                df.sort_values(by='time', ascending=False, inplace = True)
                df.to_csv(f'ticks\\{symbol}_ticksrange.csv', index=False)
        
        def slice(self, type, symbol, initial_date, final_date, timeframe=None):
            
            path = (
                os.path.join('ohlc', timeframe, f'{symbol}_{timeframe}.csv')
                if type == 'ohlc'
                else os.path.join('ticks', timeframe, f'{symbol}_ticksrange.csv')
            )
            
            if not os.path.exists(path):
                print('ativo não registrado, use .update_{type}')
            else:
                df = pd.read_csv(path)
                df['time'] = pd.to_datetime(df['time'])
                return df.loc[(df['time'] >= initial_date) & (df['time'] < final_date)]
        
        def read_ohlc(self, symbol, timeframe, initial_date=datetime(2012,1,1), final_date=datetime.now()):
            return self.slice('ohlc', symbol, initial_date, final_date, timeframe)
            
        def read_ohlc(self, symbol, initial_date=datetime(2012,1,1), final_date=datetime.now()):
            return self.slice('ticks', symbol, initial_date, final_date, timeframe)