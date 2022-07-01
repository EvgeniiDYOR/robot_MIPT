#!/usr/bin/python3

from pickle import TRUE
from pyrob.api import *


@task
def task_8_22():

    def corner():
        if (wall_is_above() == True and 
            wall_is_on_the_left() == True):
            while wall_is_on_the_right() != True:
                move_right()

        elif (wall_is_above() == True and 
              wall_is_on_the_right() == True):
            while wall_is_on_the_left() != True:
                move_left()

        elif (wall_is_beneath() == True and 
              wall_is_on_the_left() == True):
            while wall_is_on_the_right() != True:
                move_right()

        elif (wall_is_beneath() == True and 
              wall_is_on_the_right() == True):
            while wall_is_on_the_left() != True:
                move_left()
    
    if wall_is_above() != True:
        while wall_is_above() != True:
            move_up()
        corner()
    elif wall_is_beneath() != True:
        while wall_is_beneath() != True:
            move_down()
        corner()
    elif wall_is_on_the_left() != True:
        while wall_is_on_the_left() != True:
            move_left()
        corner()
    elif wall_is_on_the_right() != True:
        while wall_is_on_the_right() != True:
            move_right()


if __name__ == '__main__':
    run_tasks()
