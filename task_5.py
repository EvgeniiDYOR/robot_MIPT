#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    for i in range(10):
        if wall_is_beneath() == True:
            move_right()   


if __name__ == '__main__':
    run_tasks()
