import datetime


def main():
    time1 = datetime.datetime.now()
    if time1.hour<19:
        time2=datetime.datetime(time1.year,time1.month,time1.day,19,0,0)
        result=time2-time1
        print(result)

if __name__=='__main__':
    main()