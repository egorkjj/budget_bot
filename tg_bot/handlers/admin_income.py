from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from tg_bot.states import income
from tg_bot.keyboards import manager_kb_income, types_income, income_decline, is_cash_income_kb, income_payment
from tg_bot.DBSM import add_income
def register_handlers_income(dp: Dispatcher):
    dp.register_message_handler(add_income_step1, commands=["income"])
    dp.register_callback_query_handler(add_income_step2, text_startswith = "income_manager", state = income.select_manager)
    dp.register_callback_query_handler(select_income_is_cash, text_startswith = "income_cash", state = income.select_is_cash)
    dp.register_callback_query_handler(add_income_step3, text_startswith = "income_type", state = income.select_type)
    dp.register_message_handler(add_income_comment, state = income.type_comment)
    dp.register_message_handler(add_income_step5, state = income.type_summ)
    dp.register_callback_query_handler(add_income_step6, state = income.type_order, text_startswith = "income_payment")
    dp.register_message_handler(add_income_step7, state = income.type_fio)
    dp.register_callback_query_handler(decline_add_income, state = "*", text = "decline_income")
    
async def add_income_step1(message: types.Message, state: FSMContext): # начало
    await message.answer("Для начала, представьтесь, пожалуйста", reply_markup=manager_kb_income())
    await income.select_manager.set()

async def add_income_step2(call: types.CallbackQuery, state: FSMContext): #выбрал имя
    async with state.proxy() as data:
        data["manager_income"] = call.data.split("_")[2]
    await call.message.answer(f"Хорошо, {call.data.split('_')[2]}, теперь выберите формат дохода", reply_markup = is_cash_income_kb())
    await income.select_is_cash.set()

async def select_income_is_cash(call: types.CallbackQuery, state: FSMContext): #выбрал формат
    is_cash = bool(int(call.data.split("_")[2]))
    async with state.proxy() as data:
        data["is_cash"] = is_cash

    if is_cash:
        async with state.proxy() as data:
            data["type_income"] = "отсутствует"
        await call.message.answer("Хорошо, введите комментарий", reply_markup=income_decline())
        await income.type_comment.set()
    else:
        await income.select_type.set()
        await call.message.answer("Хорошо, теперь выберите тип дохода", reply_markup= types_income())

async def add_income_step3(call: types.CallbackQuery, state: FSMContext): #выбрал категорию
    async with state.proxy() as data:
        data["type_income"] = call.data.split("_")[2]
    await call.message.answer("Хорошо, введите комментарий", reply_markup=income_decline())
    await income.type_comment.set()
    

async def add_income_comment(message: types.Message, state: FSMContext): #пишет коммент
    async with state.proxy() as data:
        data["comment_income"] = message.text
    await message.answer("Комментарий принят. Теперь введите сумму дохода в бел.руб.", reply_markup= income_decline())
    await income.type_summ.set()

async def add_income_step5(message: types.Message, state: FSMContext):
    try:
        float(message.text.replace(",", "."))
    except ValueError:
        await message.answer("Упс, такого числа не существует... Введите, пожалуйста, еще раз", reply_markup= income_decline())
        return
    
    async with state.proxy() as data:
        data["summ_income"] = float(message.text.replace(",", "."))
    await message.answer("Выберите тип оплаты в заказе", reply_markup= income_payment())
    await income.type_order.set()

async def add_income_step6(call: types.CallbackQuery, state: FSMContext):
    pay = call.data.split("_")[2]
    async with state.proxy() as data:
        data["payment_type"] = pay
    await call.message.answer("Хорошо, теперь введите ФИО", reply_markup= income_decline())
    await income.type_fio.set()


async def add_income_step7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["fio"] = message.text
    await message.answer("Добавление дохода завершено")

    async with state.proxy() as data:
        add_income(data["manager_income"], data["comment_income"], data["type_income"], data["summ_income"], data["is_cash"], data["payment_type"], data["fio"])
    await state.finish()

async def decline_add_income(call:types.CallbackQuery, state: FSMContext):
    if await state.get_state() in ["income:select_comment", "income:select_manager", "income:type_comment", "income:type_summ", "income:select_type", "income:select_is_cash"]:
        await state.finish()
        await call.message.answer("Хорошо, добавление дохода завершено")
