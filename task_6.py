#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    for i in range(10):
        move_right()
        if wall_is_beneath() == True:
            while wall_is_beneath() == True:
                move_right()
            break



if __name__ == '__main__':
    run_tasks()
