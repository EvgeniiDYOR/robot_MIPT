#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    
    def print_cross():
        for i in range(3):
            move_right()
            fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_down(2)
        fill_cell()

    move_down(2)
    print_cross()
    move_left()
    move_up(2)

if __name__ == '__main__':
    run_tasks()
