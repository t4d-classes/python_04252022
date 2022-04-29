from datetime import datetime, timedelta, date

us_independence_day = datetime(1776, 7, 4)

today = datetime.now()

print(us_independence_day)


delta = today - us_independence_day

print(delta.days)

print(datetime.now().strftime("%B %A"))

tax_day_str = "04-2022-18"

print(datetime.strptime(tax_day_str, "%m-%Y-%d"))

