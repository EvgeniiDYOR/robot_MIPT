#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():

    def print_to_wall_left():
        fill_cell()
        while wall_is_on_the_left() != True:
            fill_cell()
            move_left()
        fill_cell()
        if wall_is_beneath() != True:
            move_down()
    
    def print_to_wall_right():
        fill_cell()
        while wall_is_on_the_right() != True:
            fill_cell()
            move_right()
        fill_cell()
        if wall_is_beneath() != True:
            move_down()

    for i in range(100):
        print_to_wall_right()
        if (wall_is_beneath() == True and
            wall_is_on_the_right() == True):
            print_to_wall_left()
            break
        if (wall_is_beneath() == True and
            wall_is_on_the_left() == True):
            print_to_wall_right()
            print_to_wall_left()
            break
        print_to_wall_left()


if __name__ == '__main__':
    run_tasks()
