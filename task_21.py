#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():

    def print_triangle():
        counter = 1
        while True:
            move_right(counter)
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
            counter += 1
            move_down()
            if wall_is_beneath():
                break

    move_down()
    print_triangle()
    move_right()


if __name__ == '__main__':
    run_tasks()
