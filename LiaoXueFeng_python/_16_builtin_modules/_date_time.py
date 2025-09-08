from datetime import datetime

def test():
    now = datetime.now()
    print(now)
    print(type(now))

    dt = datetime(2025, 9, 8, 13, 33)
    print(dt)

    '''timestamp presents an interval value since 1970-1-1 00:00 UTC+00:00,
    so it has nothing to do with time zone.
    '''
    t_stamp = dt.timestamp()
    print(t_stamp)
    print(datetime.fromtimestamp(t_stamp))    #local time zone

    cday = datetime.strptime("2025-09-08 13:51:42", "%Y-%m-%d %H:%M:%S")
    print(cday)

    print(now.strftime('%a, %b %d %H:%M'))

if __name__  == "__main__":
    test()
