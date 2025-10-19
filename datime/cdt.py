from datetime import date, time, datetime

t=date.today()
n=datetime.now()

print("Today's date is: ", t)
print("\n current date and time is", n)

print("\n Date components",t.year,"-",t.month,"-",t.day)
