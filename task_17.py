#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while not cell_is_filled():
        move_up()
    while True:
        move_right()
        if cell_is_filled():
            break
        else:
            move_left(2)
            break


if __name__ == '__main__':
    run_tasks()
