from  aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

from aiohttp.helpers import call_later
from magic_filter.util import and_op
from pyexpat.errors import messages

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# button_ = KeyboardButton(text = 'Рассчитать')
# button1_ = KeyboardButton(text = 'Информация')
# button2_ = KeyboardButton(text = 'Купить')
# kb.row(button_, button1_)
# kb.row(button2_)
#
# kb2 = InlineKeyboardMarkup(resize_keyboard = True)
# button = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data= 'calories')
# button2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data= 'formulas')
# kb2.row(button, button2)

kb3 = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text= 'Product1', callback_data= 'product_buying'),
        InlineKeyboardButton(text= 'Product2', callback_data= 'product_buying'),
        InlineKeyboardButton(text= 'Product3', callback_data= 'product_buying'),
        InlineKeyboardButton(text= 'Product4', callback_data= 'product_buying')]
    ], resize_keyboard = True
)


class UserState(StatesGroup):  #собираем данные
    age = State()
    growth = State()
    weight = State()


# @dp.message_handler(commands= ['start'])
# async def start_message(message):
#     await message.answer('Привет! Я бот помогающий здоровью.', reply_markup = kb )
#
#
# @dp.message_handler(text = 'Рассчитать')
# async def main_menu(message):
#     await message.answer('Выберите опцию:', reply_markup = kb2)


@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    for number in range(1, 5):
        await message.answer(f'Название: Product{number} | Описание: описание {number} | Цена: {number * 100}')
        with open(f'bot_selling_games/{number}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup= kb3)


@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


# @dp.callback_query_handler(text= 'formulas')
# async def get_formulas(call):
#     await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
#     await call.answer()
#
#
# @dp.callback_query_handler(text = 'calories')
# async def set_age(call):
#     await call.message.answer('Введите свой возраст:')
#     await UserState.age.set()   #запись возраста
#
#
# @dp.message_handler()
# async def all_message(message):
#     await message.answer('Введите команду /start, чтобы начать общение.')
#
#
# @dp.message_handler(state = UserState.age)
# async def set_growth(message, state):
#     try:
#         await state.update_data(age = float(message.text))
#     except:
#         await message.answer('Введите число, свой возраст')
#         return set_age()
#     await message.answer('Введите свой рост в см:', )
#     await UserState.growth.set()
#
#
# @dp.message_handler(state = UserState.growth)
# async def set_weight(message, state):
#     try:
#         await state.update_data(growth = float(message.text))
#     except:
#         await message.answer('Введите число, свой рост')
#         return set_growth()
#     await message.answer('Введите свой вес:')
#     await UserState.weight.set()
#
#
# @dp.message_handler(state = UserState.weight)
# async def send_calories(message, state):
#     try:
#         await state.update_data(weight =float(message.text))
#     except:
#         await message.answer('Введите число, свой вес')
#         return send_calories()
#     data = await state.get_data()
#     calories = (10 * data['weight'] + 6.25 * data['growth'] -
#                 5 * data['age'] - 161)
#     await message.answer(f'Ваша норма калорий {calories}/сутки')
#     await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)


