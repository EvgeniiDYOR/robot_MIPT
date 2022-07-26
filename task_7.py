#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while True:
        counter = 0
        move_down()
        if wall_is_beneath():
            while wall_is_beneath():
                move_right()
                counter += 1
            move_down()
            move_left(counter)
            break


if __name__ == '__main__':
    run_tasks()
