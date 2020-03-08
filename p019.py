import datetime

sunday_count = 0
for year in range(1901,2001):
	for month in range(1,13):
		day = datetime.datetime(year,month,1)
		if day.weekday() == 6:
			sunday_count += 1
print(sunday_count)
