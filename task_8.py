#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    for i in range(20):
        move_right()
        if wall_is_above() == False and wall_is_beneath() == False:
            break





if __name__ == '__main__':
    run_tasks()
