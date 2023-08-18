from aiogram import Bot, Router
from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton, \
                            KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder


from lexicon.lexicon_ru import LEXICON_MENU_COMMANDS, LEXICON_APP_COMMANDS

router = Router()

async def  set_start_menu(bot: Bot):
    main_menu_commands = [BotCommand(command=command,
                   description=deskript) for command, deskript in LEXICON_MENU_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)

def inline_kb_generator(width: int,
                        *args: str,
                        **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_list: list[InlineKeyboardButton] = []
    if args:
        for button in args:
            kb_list.append(InlineKeyboardButton(
                            text=LEXICON_APP_COMMANDS[button]
                            if button in LEXICON_APP_COMMANDS else button,
                            callback_data=button))
    if kwargs:
        for button, data in kwargs.items():
            kb_list.append(InlineKeyboardButton(
                            text=button,
                            callback_data=data))
    kb_builder.row(*kb_list, width=width)
    return kb_builder.as_markup()

def inline_kb_appeal_list(dict_appeal: dict[str, str]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_list: list[InlineKeyboardButton] = []

    for button, data in dict_appeal.items():
        kb_list.append(InlineKeyboardButton(
                        text=data,
                        callback_data=button))
    kb_builder.row(*kb_list, width=1)

    return kb_builder.as_markup()



