#!/usr/bin/python3
import datetime as dt

def main():

    startTime = dt.datetime.now()
    mydate = dt.dateTime(1962,7, 28)
    print((startTime-mydate).seconds)


if __name__ == '__main__':
    main()

