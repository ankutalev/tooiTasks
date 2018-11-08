import time
import sys
import datetime
from random import randint
from timeit import default_timer as timer



def sleep_random_time():
    time.sleep(randint(0, 9))


def measure():
    start = timer()
    sleep_random_time()
    end = timer()
    file = open("measure.txt","w")
    print("Slept for ", end - start)
    file.write("Current date: ",)
    file.write("{:%B %d, %Y}".format(datetime.datetime.now()))
    file.write(" Slept for: ")
    file.write(str(end-start))
    file.close()


def sleep_and_repeat():
    delay = int(input("Enter time to sleep!"))
    if delay < 0:
        print("Negative time! Bye-bye!")
        exit(0)
    else:
        time.sleep(delay)
        sleep_and_repeat()


def date_calculator():
    bday = input("Enter your birthdate in format yyyy-mm-dd\n")
    birth_date = datetime.datetime.strptime(bday,'%Y-%m-%d')
    date = datetime.date.today()
    delta = date-birth_date.date()
    print("You are live ",delta.days," days\n")


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == 'sleep':
        sleep_and_repeat()
    elif sys.argv[1] == 'measure':
        measure()
    elif sys.argv[1] == 'date':
        date_calculator()
    else:
        print("Invalid argument! Expected 'sleep', 'measure' or 'date'")
        exit(0)
