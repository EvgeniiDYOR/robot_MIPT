#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    for i in range(10):
        move_right()
        if wall_is_on_the_right() == True:
            break



if __name__ == '__main__':
    run_tasks()
