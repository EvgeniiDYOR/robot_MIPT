#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():

    counter = 0
    interval = 1
    move_right()
    fill_cell()

    while wall_is_on_the_right != True:
        move_right()
        counter += 1
        if wall_is_on_the_right() == True:
            break
        if counter == interval:
            fill_cell()
            interval += 1
            counter = 0






if __name__ == '__main__':
    run_tasks()
