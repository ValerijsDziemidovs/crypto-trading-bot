from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT: str = 'TradingBot'

    #Binance
    BINANCE_PUBLIC_KEY: str
    BINANCE_SECRET_KEY: str
    
    BINANCE_MAIN_URL: str
    BINANCE_TEST_URL: str
    BINANCE_MAIN_WSS: str
    BINANCE_TEST_WSS: str


    class Config:
        env_file = 'appsettings.sh'

config = Settings()
