from aiogram.dispatcher.filters.state import StatesGroup, State

class expence(StatesGroup):
    select_manager = State()
    select_type = State()
    select_comment = State()
    type_comment = State()
    type_summ = State()

class income(StatesGroup):
    select_manager = State()
    select_is_cash = State()
    select_comment = State()
    select_type = State()
    type_summ = State()
    type_comment = State()
