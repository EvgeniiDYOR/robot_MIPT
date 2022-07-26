#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():

    counter = 0
    interval = 1
    move_right()
    fill_cell()

    while not wall_is_on_the_right():
        move_right()
        counter += 1
        if wall_is_on_the_right():
            break
        if counter == interval:
            fill_cell()
            interval += 1
            counter = 0


if __name__ == '__main__':
    run_tasks()
