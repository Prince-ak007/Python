# datetime module
from datetime import datetime, timedelta

#use ==> facebook post date, twitter tweet date, whatsapp message send date etc...

current_datetime =datetime.now()
print(current_datetime)
print("*"*28) #some extra 
print(current_datetime.second)
print(current_datetime.day)
print(current_datetime.month)
print(current_datetime.year)





print("*"*26)
print(current_datetime.date()) #date only 
print(current_datetime.time()) #time only

#date formatting 2023/10/23

formatted_date = current_datetime.strftime('%y/%m/%d %H/%M/%S')
print(formatted_date)

# Arithmetic  date-time to add date (import timedelta)

future_date = current_datetime + timedelta(days=10)
print(future_date)















