from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def manager_kb_income():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text = "Я Виталий", callback_data="income_manager_Виталий"))
    kb.add(InlineKeyboardButton(text = "Я Наталья", callback_data="income_manager_Наталья"))
    kb.add(InlineKeyboardButton(text = "Я Екатерина", callback_data="income_manager_Екатерина"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_income"))
    return kb

def types_income():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text = "Рассрочка Альфабанк", callback_data= "income_type_Рассрочка\u2009Альфабанк"))
    kb.add(InlineKeyboardButton(text = "Рассрочка Беларусбанк", callback_data= "income_type_Рассрочка\u2009Беларусбанк"))
    kb.add(InlineKeyboardButton(text = "Ерип(оплата онлайн)", callback_data= "income_type_Ерип(оплата\u2009онлайн)"))
    kb.add(InlineKeyboardButton(text = "Терминал магазин", callback_data= "income_type_Терминал\u2009магазин"))
    kb.add(InlineKeyboardButton(text = "Безнал Юр.лица", callback_data= "income_type_Безнал\u2009Юр.лица"))
    kb.add(InlineKeyboardButton(text = "Безнал Физ.лица", callback_data= "income_type_Безнал\u2009Физ.лица"))
    kb.add(InlineKeyboardButton(text = "Кредиты Физ.лица", callback_data= "income_type_Кредиты\u2009Физ.лица"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_income"))
    return kb

def is_cash_income_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Наличные", callback_data="income_cash_1"))
    kb.add(InlineKeyboardButton(text="Безнал", callback_data="income_cash_0"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_income"))
    return kb

def income_comment_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Есть", callback_data="income_comment_yes"))
    kb.add(InlineKeyboardButton(text="Нет", callback_data="income_comment_no"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_income"))
    return kb

def income_decline():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_income"))
    return kb

def income_payment():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text = "Предоплата 100%", callback_data="income_payment_Предоплата\u2009100%"))
    kb.add(InlineKeyboardButton(text="Предоплата", callback_data= "income_payment_Предоплата"))
    kb.add(InlineKeyboardButton(text="Доплата 100%", callback_data="income_payment_Доплата\u2009100%"))
    kb.add(InlineKeyboardButton(text="Доплата", callback_data="income_payment_Доплата"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_income"))
    return kb
