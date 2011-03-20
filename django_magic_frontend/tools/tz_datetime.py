import datetime

class TZ(datetime.tzinfo):
	def __init__(self,hours):
		self.hours=hours
	def utcoffset(self, dt):
		return datetime.timedelta(hours=self.hours)
	def dst(self, dt):
		return datetime.timedelta(0)

def get_datetime_by_tz(hours):
	tz=TZ(hours)
	return datetime.datetime.now(tz)

def get_datetimes_of_month(year, month):
    ret=[]
    for x in range(1,32):
		try:
			d=datetime.date(year, month,x)
			ret.append(d)
		except:
			pass
    return ret

def get_current_year_month_day():
	d=datetime.date.today()
	return d.year,d.month,d.day

