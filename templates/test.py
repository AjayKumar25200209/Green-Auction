from datetime import datetime,timedelta,date

# ctime=datetime.now().replace(second=0,microsecond=0)
# hour=timedelta(hours=1)
# print((ctime+hour).time())
# print(ctime.time())
datee=date.today()
time2=2
ctime=datetime.now().replace(microsecond=0,second=0)
stime=ctime.time()
hour=timedelta(hours=2)
etime=(ctime+hour)
print(datee)