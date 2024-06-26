from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from tg_bot.keyboards import manager_kb_exp, types_exp, exp_comment_kb, exp_decline
from tg_bot.states import expence
from tg_bot.DBSM import add_expence

def register_handlers_expence(dp: Dispatcher):
    dp.register_message_handler(add_expence_step1, commands=["expence"])
    dp.register_callback_query_handler(add_expence_step2, text_startswith = "expence_manager", state = expence.select_manager)
    dp.register_callback_query_handler(add_expence_step3, text_startswith = "expence_type", state = expence.select_type)
    dp.register_callback_query_handler(add_expence_step4, text_startswith = "expence_comment", state = expence.select_comment)
    dp.register_message_handler(add_expence_comment, state = expence.type_comment)
    dp.register_message_handler(add_expence_step5, state = expence.type_summ)
    dp.register_callback_query_handler(decline_add_expence, state = "*", text = "decline_expence")

async def add_expence_step1(message: types.Message, state: FSMContext): # начало
    await message.answer("Для начала, представьтесь, пожалуйста", reply_markup=manager_kb_exp())
    await expence.select_manager.set()

async def add_expence_step2(call: types.CallbackQuery, state: FSMContext): #выбрал имя
    async with state.proxy() as data:
        data["manager_expence"] = call.data.split("_")[2]
    await call.message.answer(f"Хорошо, {call.data.split('_')[2]}, теперь выберите категорию расхода.", reply_markup = types_exp())
    await expence.select_type.set()

async def add_expence_step3(call: types.CallbackQuery, state: FSMContext): #выбрал категорию
    async with state.proxy() as data:
        data["type_expence"] = call.data.split("_")[2]
    await call.message.answer("Хорошо, есть ли у Вас какой-нибудь комментарий к расходу?", reply_markup= exp_comment_kb())
    await expence.select_comment.set()

async def add_expence_step4(call: types.CallbackQuery, state: FSMContext): # выбрал есть ли коммент
    if call.data.split("_")[2] == "yes":
        await call.message.answer("Хорошо, введите комментарий.", reply_markup=exp_decline())
        await expence.type_comment.set()
    else:
        async with state.proxy() as data:
            data["comment_expence"] = "отсутствует"
        await call.message.answer("Хорошо, теперь введите сумму расхода в бел.руб.", reply_markup=exp_decline())
        await expence.type_summ.set()

async def add_expence_comment(message: types.Message, state: FSMContext): #пишет коммент
    async with state.proxy() as data:
        data["comment_expence"] = message.text
    await message.answer("Комментарий принят. Теперь введите сумму расхода в бел.руб.", reply_markup= exp_decline())
    await expence.type_summ.set()

async def add_expence_step5(message: types.Message, state: FSMContext):
    try:
        float(message.text.replace(",", "."))
    except ValueError:
        await message.answer("Упс, такого числа не существует... Введите, пожалуйста, еще раз", reply_markup= exp_decline())
        return
    
    async with state.proxy() as data:
        data["summ_expence"] = float(message.text.replace(",", "."))
    await message.answer("Добавление расхода завершено")

    async with state.proxy() as data:
        add_expence(data["manager_expence"], data["comment_expence"], data["type_expence"], data["summ_expence"])
    await state.finish()

async def decline_add_expence(call:types.CallbackQuery, state: FSMContext):
    if await state.get_state() in ["expence:select_comment", "expence:select_manager", "expence:type_comment", "expence:type_summ", "expence:select_type"]:
        await state.finish()
        await call.message.answer("Хорошо, добавление расхода завершено")







