from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from Fsm_keyboards.fsm_keyboard import name_keyboard, size_keyboard, location
from bot import Bot

router = Router()


class OrderFood(StatesGroup):
    waiting_food_name = State()
    waiting_food_size = State()
    waiting_place_address = State()


@router.message(Command('Food'), StateFilter(None))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer('Choose food from the given variants', reply_markup=name_keyboard())
    await state.set_state(OrderFood.waiting_food_name)


@router.callback_query(F.data == 'punch')
async def cb_punch(callback: CallbackQuery, state: FSMContext, bot: Bot):
    chat_id = callback.message.chat.id
    await state.update_data(chosen_food=callback.data)
    await bot.send_message(chat_id=chat_id, text='Choose food size', reply_markup=size_keyboard())
    await callback.answer()
    await state.set_state(OrderFood.waiting_food_size)


@router.callback_query(F.data == 'pie')
async def cb_pie(callback: CallbackQuery, state: FSMContext, bot: Bot):
    chat_id = callback.message.chat.id
    await state.update_data(chosen_food=callback.data)
    await bot.send_message(chat_id=chat_id, text='Choose food size', reply_markup=size_keyboard())
    await callback.answer()
    await state.set_state(OrderFood.waiting_food_size)


@router.callback_query(F.data == 'pizza')
async def cb_pizza(callback: CallbackQuery, state: FSMContext, bot: Bot):
    chat_id = callback.message.chat.id
    await state.update_data(chosen_food=callback.data)
    await bot.send_message(chat_id=chat_id, text='Choose food size', reply_markup=size_keyboard())
    await callback.answer()
    await state.set_state(OrderFood.waiting_food_size)


@router.callback_query(F.data == 'large')
async def cb_large(callback: CallbackQuery, state: FSMContext, bot: Bot):
    chat_id = callback.message.chat.id
    await state.update_data(chosen_size=callback.data)
    await bot.send_message(chat_id=chat_id, text='Choose place for delivery', reply_markup=location())
    await callback.answer()
    await state.set_state(OrderFood.waiting_place_address)


@router.callback_query(F.data == 'major')
async def cb_major(callback: CallbackQuery, state: FSMContext, bot: Bot):
    chat_id = callback.message.chat.id
    await state.update_data(chosen_size=callback.data)
    await bot.send_message(chat_id=chat_id, text='Choose place for delivery', reply_markup=location())
    await callback.answer()
    await state.set_state(OrderFood.waiting_place_address)


@router.callback_query(F.data == 'small')
async def cb_small(callback: CallbackQuery, state: FSMContext, bot: Bot):
    chat_id = callback.message.chat.id
    await state.update_data(chosen_size=callback.data)
    await bot.send_message(chat_id=chat_id, text='Choose place for delivery', reply_markup=location())
    await callback.answer()
    await state.set_state(OrderFood.waiting_place_address)


@router.message(OrderFood.waiting_place_address, F.location)
async def cmd_location(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(text=f'Your order is received, thank you for using bot\nEnjoy your {user_data["chosen_size"]} {user_data["chosen_food"]}', reply_markup=ReplyKeyboardRemove())
    await state.clear()
