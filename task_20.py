#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    def move_print_left(x):
        for i in range(x):
            fill_cell()
            move_left() 
        fill_cell()        
    
    def move_print_right(x):
        for i in range(x):
            fill_cell()
            move_right()
        fill_cell()

    move_right()
    for i in range(6):
        move_print_right(26)
        move_down()
        move_print_left(26)
        move_down()


if __name__ == '__main__':
    run_tasks()
