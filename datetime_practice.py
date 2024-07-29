from datetime import date, time, timedelta, datetime, timezone

d = date(2024, 7, 1)
print(d.year)
print(d.month)
print(d.day)

t = time(14, 30, 30, 0)
print((t.hour, t.minute, t.second, t.microsecond))

start = datetime(2024, 7, 1, 14, 30, 0)

end = datetime(2024, 7, 3, 10, 0, 0)

duration = end - start

print(duration.days, duration.min, duration.seconds)

td = timedelta(days=2, hours=12)
new_date = start + td

print(new_date)

# Printing utc +5:30
tz = timezone(timedelta(hours=5, minutes=30))

print(tz)
