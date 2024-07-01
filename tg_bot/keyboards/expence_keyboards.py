from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def manager_kb_exp():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text = "Я Виталий", callback_data="expence_manager_Виталий"))
    kb.add(InlineKeyboardButton(text = "Я Наталья", callback_data="expence_manager_Наталья"))
    kb.add(InlineKeyboardButton(text = "Я Екатерина", callback_data="expence_manager_Екатерина"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_expence"))
    return kb

def types_exp():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text = "Авансы", callback_data= "expence_type_Авансы"))
    kb.add(InlineKeyboardButton(text = "Топливо", callback_data= "expence_type_Топливо"))
    kb.add(InlineKeyboardButton(text = "Запчасти", callback_data= "expence_type_Запчасти"))
    kb.add(InlineKeyboardButton(text = "Хозрасходы", callback_data= "expence_type_Хозрасходы"))
    kb.add(InlineKeyboardButton(text = "Скидки/рекламации/возврат", callback_data= "expence_type_Скидки/рекламации/возврат"))
    kb.add(InlineKeyboardButton(text = "Прочее", callback_data= "expence_type_Прочее"))
    kb.add(InlineKeyboardButton(text = "Расходы шефа", callback_data= "expence_type_Расходы\u2009шефа"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_expence"))
    return kb

def exp_comment_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Есть", callback_data="expence_comment_yes"))
    kb.add(InlineKeyboardButton(text="Нет", callback_data="expence_comment_no"))
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_expence"))
    return kb

def exp_decline():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text = "Отменить добавление ❌", callback_data="decline_expence"))
    return kb







