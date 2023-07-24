import kb as kb
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from venv.constants import *


API_TOKEN = "6111571414:AAGlf3pF9lrCLZZZ0p-VOztM8ygGLJ7iDfM"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class TestState(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_0 = ListItem()
    TEST_STATE_1 = ListItem()
    TEST_STATE_2 = ListItem()
    TEST_STATE_3 = ListItem()
    TEST_STATE_4 = ListItem()
    TEST_STATE_5 = ListItem()


@dp.message_handler(Text("Главное меню"), state="*")
@dp.message_handler(commands=["start"], state="*")
async def cmd_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    kb = [
        [types.KeyboardButton(text="Что такое Atomy?")],
        [types.KeyboardButton(text="О бизнесе")],
        [types.KeyboardButton(text="Наша продукция")],
        [types.KeyboardButton(text="Система для продвижения")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    await state.set_state(TestState.all()[0])
    await message.answer(
        firstPage,
        reply_markup=keyboard,
    )


@dp.message_handler(Text("Что такое Atomy?"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Почему именно Atomy?")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(whyAtomy, reply_markup=keyboard)


@dp.message_handler(Text("О бизнесе"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="За что и сколько платит компания ")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(aboutBusiness, reply_markup=keyboard)


@dp.message_handler(Text("Шаг Назад"), state=TestState.TEST_STATE_4)
@dp.message_handler(Text("Наша продукция"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Здоровье")],
        [types.KeyboardButton(text="Уход за волосами")],
        [types.KeyboardButton(text="Уход за кожей")],
        [types.KeyboardButton(text="Уход за полостью рта")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[4])
    await message.answer(ourProduct, reply_markup=keyboard)


@dp.message_handler(Text("Здоровье"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Хочу заказать")],
        [types.KeyboardButton(text="Шаг Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await message.answer(health, reply_markup=keyboard)


@dp.message_handler(Text("Хочу заказать"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await message.answer(endOrder, reply_markup=keyboard)


@dp.message_handler(Text("Уход за волосами"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Хочу заказать")],
        [types.KeyboardButton(text="Шаг Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await message.answer(hair, reply_markup=keyboard)


@dp.message_handler(Text("Уход за кожей"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Хочу заказать")],
        [types.KeyboardButton(text="Шаг Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await message.answer(derma, reply_markup=keyboard)


@dp.message_handler(Text("Уход за полостью рта"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Хочу заказать")],
        [types.KeyboardButton(text="Шаг Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await message.answer(mouth, reply_markup=keyboard)


@dp.message_handler(Text("Назад"), state=TestState.TEST_STATE_3)
@dp.message_handler(Text("Система для продвижения"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Торговый представитель")],
        [types.KeyboardButton(text="Агент")],
        [types.KeyboardButton(text="Специальный агент")],
        [types.KeyboardButton(text="Дилер")],
        [types.KeyboardButton(text="Эксклюзивный дистрибьютор")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder = "Выберите значение",
    )
    state = dp.current_state(user=message.from_user.id)
    await message.answer(goSystem, reply_markup=keyboard)


@dp.message_handler(Text("Почему именно Atomy?"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Расскажи мне о бизнесе в Atomy")],
        [types.KeyboardButton(text="Главное меню")]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(whyIsAtomy, reply_markup=keyboard)


@dp.message_handler(Text("Расскажи мне о бизнесе в Atomy"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="За что и примерно сколько платит мне компания")],
        [types.KeyboardButton(text="Главное меню")]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(aboutBusiness, reply_markup=keyboard)


@dp.message_handler(Text("За что и примерно сколько платит мне компания"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Посмотреть видео")],
        [types.KeyboardButton(text="Давай ты мне расскажешь")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(whoIsPayments, reply_markup=keyboard)


@dp.message_handler(Text("За что и сколько платит компания"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Посмотреть видео")],
        [types.KeyboardButton(text="Давай ты мне расскажешь")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(whoIsPayments, reply_markup=keyboard)


@dp.message_handler(Text("Давай ты мне расскажешь"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Классификация и условия дистрибьюторства")],
        [types.KeyboardButton(text="Спонсорское вознаграждение")],
        [types.KeyboardButton(text="Мастерское вознаграждение")],
        [types.KeyboardButton(text="Условия повышения уровня мастерства")],
        [types.KeyboardButton(text="Бонусы и поощрения для мастеров")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(manual, reply_markup=keyboard)


@dp.message_handler(Text("Условия повышения уровня мастерства"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Мастерское вознаграждение")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(upgradeMaster, reply_markup=keyboard)


@dp.message_handler(Text("Классификация и условия дистрибьюторства"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Торговый представитель")],
        [types.KeyboardButton(text="Агент")],
        [types.KeyboardButton(text="Специальный агент")],
        [types.KeyboardButton(text="Дилер")],
        [types.KeyboardButton(text="Эксклюзивный дистрибьютор")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(goSystem, reply_markup=keyboard)


@dp.message_handler(Text("Торговый представитель"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Агент")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[3])
    await message.answer(sellPerson, reply_markup=keyboard)


@dp.message_handler(Text("Агент"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Специальный агент")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[3])
    await message.answer(agent, reply_markup=keyboard)


@dp.message_handler(Text("Специальный агент"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Дилер")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[3])
    await message.answer(specialAgent, reply_markup=keyboard)


@dp.message_handler(Text("Дилер"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Эксклюзивный дистрибьютор")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[3])
    await message.answer(diler, reply_markup=keyboard)


@dp.message_handler(Text("Эксклюзивный дистрибьютор"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Мастерское вознаграждение")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[3])
    await message.answer(diler, reply_markup=keyboard)


@dp.message_handler(Text("Спонсорское вознаграждение"), state="*")
async def with_puree(message: types.Message):

    kb = [
        [types.KeyboardButton(text="Мастерское вознаграждение")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(sponsorPrice, reply_markup=keyboard)


@dp.message_handler(Text("Назад"), state=TestState.TEST_STATE_2)
@dp.message_handler(Text("Мастерское вознаграждение"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Мастер продаж")],
        [types.KeyboardButton(text="Бриллиантовый мастер")],
        [types.KeyboardButton(text="Мастер Шаронской Розы")],
        [types.KeyboardButton(text="Стар Мастер")],
        [types.KeyboardButton(text="Роял Мастер")],
        [types.KeyboardButton(text="Краун Мастер")],
        [types.KeyboardButton(text="Империал Мастер")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[2])
    await message.answer(masterPrice, reply_markup=keyboard)


@dp.message_handler(Text("Мастер продаж"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Бриллиантовый мастер")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await state.set_state(TestState.all()[2])
    await message.answer(sellMaster, reply_markup=keyboard)


@dp.message_handler(Text("Бриллиантовый мастер"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Мастер Шаронской Розы")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await state.set_state(TestState.all()[2])
    await message.answer(diamondMaster, reply_markup=keyboard)


@dp.message_handler(Text("Мастер Шаронской Розы"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Стар Мастер")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[2])
    await message.answer(masterRose, reply_markup=keyboard)


@dp.message_handler(Text("Стар Мастер"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Роял Мастер")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[2])
    await message.answer(starMaster, reply_markup=keyboard)


@dp.message_handler(Text("Роял Мастер"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Краун Мастер")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[2])
    await message.answer(royalMaster, reply_markup=keyboard)


@dp.message_handler(Text("Краун Мастер"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Империал Мастер")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[2])
    await message.answer(crownMaster, reply_markup=keyboard)


@dp.message_handler(Text("Империал Мастер"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Как стать партнером Atomy?")],
        [types.KeyboardButton(text="Условия повышения уровня мастерства")],
        [types.KeyboardButton(text="Назад")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[2])
    await message.answer(imperialMaster, reply_markup=keyboard)


@dp.message_handler(Text("Как стать партнером Atomy?"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[2])
    await message.answer(endMessage, reply_markup=keyboard)


@dp.message_handler(Text("Посмотреть видео"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Мне всё понятно. Хочу стать партнёром!")],
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(video, reply_markup=keyboard)


@dp.message_handler(Text("Мне всё понятно. Хочу стать партнёром!"), state="*")
async def with_puree(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи",
    )
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(TestState.all()[1])
    await message.answer(endMessage, reply_markup=keyboard)


@dp.message_handler()
async def echo(message: types.message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

