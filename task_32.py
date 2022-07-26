#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    counter = 0
    while True:
        if wall_is_above():
            fill_cell()
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    counter += 1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        move_right()
        if wall_is_on_the_right():
            break

    mov('ax', counter)


if __name__ == '__main__':
    run_tasks()
