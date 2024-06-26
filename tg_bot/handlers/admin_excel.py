from openpyxl import Workbook as WB
from openpyxl.styles import Font, Alignment
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from tg_bot.DBSM import review_for_day_for_managers
import os
from datetime import datetime
import pytz

def register_excel(dp: Dispatcher):
    dp.register_message_handler(cash_reviews_for_today, commands = ["cash"])
    dp.register_message_handler(month_excel, commands = ["month"])

async def cash_reviews_for_today(message: types.Message, state: FSMContext):
    data = review_for_day_for_managers()
    result = data[0]
    cash_res = data[1]
    wb = WB()
    wb.remove(wb["Sheet"])
    sheet1 = wb.create_sheet("Виталий", 0)
    sheet2 = wb.create_sheet("Наталья", 1)
    sheet3 = wb.create_sheet("Екатерина", 2)
    sheets = [sheet1, sheet2, sheet3]
    for sheet in sheets:
        sheet["A1"] = "Доход/расход"
        sheet['A1'].font = Font(color="FF0000")
        sheet["B1"] = "Категория"
        sheet['B1'].font = Font(color="FF0000")
        sheet["C1"] = "Комментарий"
        sheet['C1'].font = Font(color="FF0000")
    for i in range(3):
        shit = sheets[i]
        query = result[i]
        cash = cash_res[i]
        for j in range(len(query)):
            shit[f"A{j+2}"] = "Доход" if query[j]["is_income"] else "Расход"
            shit[f"B{j+2}"] = query[j]["type"] if query[j]["type"] != "отсутствует" else "-"
            shit[f"C{j+2}"] = query[j]["comment"] if query[j]["comment"] != "отсутствует" else "❌"
        row = len(query) + 2
        shit.merge_cells(f"B{row}:C{row}")
        shit.merge_cells(f"B{row+1}:C{row+1}")
        shit[f"B{row+1}"] = f"{cash} бел.руб."
        shit[f"B{row}"] = "Итого"
        shit[f"B{row}"].font = Font(color = "00FF00")
        shit[f"B{row+1}"].font = Font(color = "00FF00")
        shit[f"B{row}"].alignment = Alignment(horizontal= "center")
        shit[f"B{row+1}"].alignment = Alignment(horizontal= "center")

    if not os.path.isdir("tg_bot/excel"):
        os.mkdir("tg_bot/excel")
    date = datetime.strftime(datetime.now(pytz.timezone('Europe/Moscow')), "%d.%m.%Y")
    wb.save(f"tg_bot/excel/Касса {date}.xlsx")
    await message.answer_document(document = InputFile(f"tg_bot/excel/Касса {date}.xlsx"))
    os.remove(f"tg_bot/excel/Касса {date}.xlsx")






