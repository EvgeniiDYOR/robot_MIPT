#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    
    counter = 0

    while counter != 3:
        move_right()
        if cell_is_filled() == True:
            counter += 1
        else:
            counter = 0
        if wall_is_on_the_right() == True:
            break
  


if __name__ == '__main__':
    run_tasks()
