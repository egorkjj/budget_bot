import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()

early = today.replace(day = 1, hour= 0, minute= 0, second= 0, microsecond= 0)
late = early + relativedelta(months = 1)
print(late)
