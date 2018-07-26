import time
from scheduler import Scheduler


def good_task_1():
    print('Good Task 1')


def good_task_2():
    print('Good Task 2')


def good_task_3():
    print('Good Task 3')


def bad_task_1():
    print('Bad Task 1')
    print(1/0)


def bad_task_2():
    print('Bad Task 2')
    raise Exception('Something went wrong!')


scheduler = Scheduler(interval=3, task=good_task_1)
scheduler.start()
# scheduler.every(3).seconds.do(good_task_1)
# scheduler.every(5).seconds.do(bad_task_1)
# scheduler.every(7).seconds.do(good_task_2)
# scheduler.every(8).seconds.do(bad_task_2)
# scheduler.every(12).seconds.do(good_task_3)

while True:
    scheduler.run_pending()
    time.sleep(1)