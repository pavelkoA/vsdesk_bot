from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class DataBase:
    db_name: str
    db_url: str
    db_user: str
    db_password: str

@dataclass
class Config:
    tgbot: TgBot
    # database: DataBase

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env()
    return Config(tgbot=TgBot(token=env('BOT_TOKEN'),
                        admin_ids=env('ADMIN_IDS')))
                        # database=DataBase(db_name=env('DATABASE'),
                        # db_url=env('BD_ADDRESS'),
                        # db_user=env('BD_USER'),
                        # db_password=env('BD_PASSWORD')))

