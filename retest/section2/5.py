
#5.current year,month,day

from datetime import datetime
current_date=datetime.now()
current_year=current_date.year
current_month=current_date.month
current_day=current_date.day

print("year:",current_year)
print("month:",current_month)
print("day:",current_day)
