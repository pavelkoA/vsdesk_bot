import asyncio

from aiogram import Bot, Dispatcher, Router

from config_data.config import load_config, Config
from handlers import user_handlers
from keyboards import keyboards

async def main():

    config: Config = load_config()

    bot: Bot = Bot(token=config.tgbot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)

    await keyboards.set_start_menu(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('Ahtung!!! Bot stopped!!!')


