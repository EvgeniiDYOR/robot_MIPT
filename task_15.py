#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if (wall_is_above() == True and 
        wall_is_on_the_left() == True):
        while wall_is_beneath() != True:
            move_down()
        while wall_is_on_the_right() != True:
            move_right()

    elif (wall_is_above() == True and 
        wall_is_on_the_right() == True):
        while wall_is_beneath() != True:
            move_down()
        while wall_is_on_the_left() != True:
            move_left()

    elif (wall_is_beneath() == True and 
        wall_is_on_the_left() == True):
        while wall_is_above() != True:
            move_up()
        while wall_is_on_the_right() != True:
            move_right()

    elif (wall_is_beneath() == True and 
        wall_is_on_the_right() == True):
        while wall_is_above() != True:
            move_up()
        while wall_is_on_the_left() != True:
            move_left()




if __name__ == '__main__':
    run_tasks()
