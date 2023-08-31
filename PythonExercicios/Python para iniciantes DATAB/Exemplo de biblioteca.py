from datetime import date
from datetime import datetime

hoje = date.today()
print(hoje)
futuro = date(day= 20, month= 3, year=2024)
print(futuro)
futuro = futuro.replace(month = 7)
print(futuro)
agora = datetime.now()
print(agora)