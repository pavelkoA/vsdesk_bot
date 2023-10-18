from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, CallbackQuery
from aiogram.filters import CommandStart, Command, Text, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from keyboards import keyboards
from lexicon.lexicon_ru import LEXICON_APP_COMMANDS, LEXICON_APP_TEXT
from external_services import request

import json

router: Router = Router()

class FSMCurrentAppealView(StatesGroup):
    current_appeal_list = State()
    close_appeal_list = State()
    appeal_view = State()

@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_press(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_APP_TEXT['cancel_not_state'],
                         reply_markup=keyboards.inline_kb_generator(1, 'my_app', 'my_close_app'))


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_press(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_APP_TEXT['start_text'],
                         reply_markup=keyboards.inline_kb_generator(1, 'my_app', 'my_close_app'))



@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext):
    with open("data/user_requests/user_data.json", 'r', encoding='utf-8') as json_file:
        for key, value in json.load(json_file).items():
            if int(message.from_user.id) in value["treners_id"]:
                await state.update_data(value)
                break
    await message.answer(text=LEXICON_APP_TEXT['start_text'],
                         reply_markup=keyboards.inline_kb_generator(1, 'my_app', 'my_close_app'))

@router.message(Command(commands=['start', 'help']), ~StateFilter(default_state))
async def process_start_not_default_state(message:Message):
    await message.answer(text=LEXICON_APP_TEXT['start_not_default_state_text'])

@router.callback_query(Text(text='my_app'), StateFilter(default_state))
async def process_my_app_press(callback: CallbackQuery, state: FSMContext):
    data_dict = await state.get_data()
    await callback.message.answer(text=LEXICON_APP_TEXT['current_app_text'],
                          reply_markup=keyboards.inline_kb_appeal_list(
                              request.all_request_dict(data_dict["headers"], data_dict["payload"], data_dict["cookie"])
                          ))
    await state.set_state(FSMCurrentAppealView.current_appeal_list)

@router.callback_query(StateFilter(FSMCurrentAppealView.current_appeal_list))
async def process_request_press(callback: CallbackQuery, state: FSMContext):
    data_dict = await state.get_data()
    await callback.message.answer(text=request.request_data(callback.data, data_dict["headers"], data_dict["payload"], data_dict["cookie"]))
    await state.set_state(FSMCurrentAppealView.appeal_view)

