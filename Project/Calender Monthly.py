import calendar
year=int(input('Enter Year: '))
N=int(input('Enter Case: '))

for i in range(N):
    month=int(input('Enter Month: '))
    print(calendar.month(year,month))