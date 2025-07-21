from datetime import datetime
now = datetime.now()
print(now)

today = datetime.today().date()
print(today)

now = datetime.now().time()
print(now)

formatted = now.strftime("%d-%m-%y %H:%M:%S")
print(formatted)