#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():

    def move_to_wall_down():
        while wall_is_beneath() != True:
            move_down()

    def move_to_wall_left():
        while wall_is_on_the_left() != True:
            move_left()
            if wall_is_beneath() != True:
                move_to_wall_down()
                return False
        return True

    def move_to_wall_right():
        while wall_is_on_the_right() != True:
            move_right()
            if wall_is_beneath() != True:
                move_to_wall_down()
                return False
        return True

    finish = False

    while finish != True:       
        if (move_to_wall_right() and 
            move_to_wall_left() == True):
            finish = True
    


    


if __name__ == '__main__':
    run_tasks()
