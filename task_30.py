#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():

    line_size = 0
    while not wall_is_on_the_right():
        move_right()
        line_size += 1

    while line_size > 0:
        for i in range(line_size):
            move_down()
            if i+1-line_size == 0:
                break
            fill_cell()
        for i in range(line_size):
            move_left()
            if i+1-line_size == 0:
                break
            fill_cell()
        for i in range(line_size):
            move_up()
            if i+1-line_size == 0:
                break
            fill_cell()
        for i in range(line_size):
            move_right()
            if i+1-line_size == 0:
                break
            fill_cell()
        move_down()
        move_left()
        line_size -= 2

    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
