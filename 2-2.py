import datetime

year, month, day = map(int, input().split())
input_date = datetime.date(year, month, day)
input_date = input_date + datetime.timedelta(days=int(input()))
print(input_date.year, input_date.month, input_date.day)
