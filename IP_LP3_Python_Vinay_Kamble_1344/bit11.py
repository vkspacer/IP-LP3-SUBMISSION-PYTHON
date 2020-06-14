date=input().split(',')
import datetime
print(datetime.date(int(date[0]),int(date[1]),int(date[2])).isocalender()[1])