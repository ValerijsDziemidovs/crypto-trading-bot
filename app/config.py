from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT: str = 'TradingBot'

    #Binance
    BINANCE_PUBLIC_KEY: str
    BINANCE_SECRET_KEY: str


    class Config:
        env_file = 'appsettings.sh'

config = Settings()
