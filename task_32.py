#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    counter = 0
    finish = False
    
    def print_up(counter):
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                counter += 1
            else:
                fill_cell()
        fill_cell()
        return counter
    
    def move_to_wall_down():
        while not wall_is_beneath():
            move_down()

    while not finish:
        if cell_is_filled():
            counter += 1
        if wall_is_above():
            fill_cell()
        move_right()
        if wall_is_on_the_right():
            finish = True
            break
        if not wall_is_above():
            counter = print_up(counter)
            move_to_wall_down()
    mov('ax', counter)


if __name__ == '__main__':
    run_tasks()
