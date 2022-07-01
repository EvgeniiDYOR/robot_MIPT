#!/usr/bin/python3

from pyrob.api import *


@task

def task_8_10():
    def color():
        if wall_is_beneath() != True:
            move_down()
            fill_cell()
            move_up()
        if wall_is_above() != True:
            move_up()
            fill_cell()
            move_down() 

    while wall_is_on_the_right() != True:
        color()
        move_right() 
    color() 



if __name__ == '__main__':
    run_tasks()
