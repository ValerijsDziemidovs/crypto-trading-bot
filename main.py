import tkinter as tk
from app.connectors.binance_futures import BinanceFuturesClient
from app.config import config
from logger import logger


if __name__=='__main__':
    binance = BinanceFuturesClient(config.BINANCE_PUBLIC_KEY, config.BINANCE_SECRET_KEY, True)




    #print(binance.get_contracts())
    #print(binance.get_bid_ask('BTCUSDT'))
    #print(binance.get_historical_candles('BTCUSDT', '1h'))
    #print(binance.get_balances())
    #print(binance.place_order('BTCUSDT', 'BUY', 0.01, 'LIMIT', 1, 'GTC'))
    #print(binance.get_order_status('BTCUSDT', 3040697811))
    #print(binance.cancel_order('BTCUSDT', 3040697811))
    

    #root = tk.Tk()
    #root.mainloop()
    