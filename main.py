import tkinter as tk
import logging
from app.connectors.binance_futures import BinanceFuturesClient
from app.config import config


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__=='__main__':
    binance = BinanceFuturesClient(config.BINANCE_PUBLIC_KEY, config.BINANCE_SECRET_KEY, True)

    #print(binance.get_contracts())
    #print(binance.get_bid_ask('BTCUSDT'))
    #print(binance.get_historical_candles('BTCUSDT', '1h'))
    print(binance.get_balances())

    #root = tk.Tk()
    #root.mainloop()
    