import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5582671089:AAFDCIOZL2SJ1aeRO1eFys44GZhSb5gpz-E'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='Start')
async def start_handler(message: types.Message):
    kb = [
        [types.KeyboardButton(text='СОЗДАТЬ ЗАЯВКУ')],
        [types.KeyboardButton(text=f'МОИ ЗАЯВКИ')]
    ]

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите что Вас интересует"
    )
    await message.reply(f'Hi {user_name} {user_id}', reply_markup=keyboard)
async def on_startup(dispatcher: Dispatcher) -> None:
    await bot.set_my_commands([
        types.BotCommand("start", "it is start command..."),
        types.BotCommand("help",  "it is help command...")
    ])

if __name__ == '__main__':
    executor.start_polling(dp)