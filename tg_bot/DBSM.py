from sqlalchemy import create_engine, Column, Integer, Text, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pytz
from dateutil.relativedelta import relativedelta


DATABASE_URL = f"sqlite:///db.sqlite3"

# Создание объекта Engine
engine = create_engine(DATABASE_URL)

# Создание базового класса для моделей
Base = declarative_base()


class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, autoincrement=True, primary_key=True)
    is_cash = Column(Boolean, nullable=True)
    manager = Column(Text, nullable=True)
    income_type = Column(Integer, nullable=True)
    comment = Column(Text, nullable=True)
    summ = Column(Float, nullable=True)
    date = Column(DateTime, nullable=True)

class Expences(Base):
    __tablename__ = "expences"
    id = Column(Integer, autoincrement=True, primary_key=True)
    manager = Column(Text, nullable=True)
    expence_type = Column(Text, nullable=True)
    comment = Column(Text, nullable=True)
    summ = Column(Float, nullable=True)
    date = Column(DateTime, nullable=True)



def add_expence(manager, comment, type, summ):
    Session = sessionmaker()
    session = Session(bind = engine)
    date_now = datetime.now(pytz.timezone('Europe/Moscow'))
    new = Expences(manager = manager, expence_type = type, summ = summ, comment = comment, date = date_now)
    session.add(new)
    session.commit()
    session.close()

def add_income(manager, comment, type, summ, is_cash):
    Session = sessionmaker()
    session = Session(bind = engine)
    date_now = datetime.now(pytz.timezone('Europe/Moscow'))
    new = Incomes(manager = manager, income_type = type, summ = summ, comment = comment, is_cash = is_cash, date = date_now)
    session.add(new)
    session.commit()
    session.close()

def review_for_day_for_managers():
    Session = sessionmaker()
    session = Session(bind = engine)
    cash_res = []
    result = []
    now = datetime.now(pytz.timezone('Europe/Moscow'))
    earliest_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    latest_today = now.replace(hour=23, minute=59, second=59, microsecond=999999)
    for i in ["Виталий", "Наталья", "Екатерина"]:
        subresult = []
        query_incomes = session.query(Incomes).filter(Incomes.manager == i, Incomes.date > earliest_today, Incomes.date < latest_today).all()
        sum_incomes = 0
        for j in query_incomes:
            if j.is_cash:
                sum_incomes += j.summ
                subresult.append({
                    "is_income": True,
                    "type": j.income_type,
                    "comment": j.comment
                })
        query_expences = session.query(Expences).filter(Expences.manager == i, Expences.date > earliest_today, Expences.date < latest_today).all()
        sum_expences = 0
        for j in query_expences:
            sum_expences += j.summ
            subresult.append({
                "is_income": False,
                "type": j.expence_type,
                "comment": j.comment
            })
        cash_summ = sum_incomes - sum_expences
        cash_summ = round(cash_summ, 2)
        result.append(subresult)
        cash_res.append(cash_summ)
    session.close()
    return [result, cash_res]

def month_rev():
    today = datetime.now(pytz.timezone('Europe/Moscow'))
    early = today.replace(day = 1, hour= 0, minute= 0, second= 0, microsecond= 0)
    late = early + relativedelta(months = 1)

Base.metadata.create_all(engine)
