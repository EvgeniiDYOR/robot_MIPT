#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    flag_wall_right = False
    flag_wall_down = False
    
    def print_cross(flag1=False, flag2=False):
        for i in range(2):
            fill_cell()
            move_right()
            fill_cell()
            if wall_is_on_the_right():
                flag1 = True
        move_left()
        move_up()
        fill_cell()
        move_down(2)
        if flag1:
            if wall_is_beneath():
                flag2 = True
        fill_cell()
        move_up()
        move_left()
        return flag1, flag2

    def move_to_wall_left():
        while not wall_is_on_the_left():
            move_left()
    
    move_down()
    while not flag_wall_down:
        flag_wall_right, flag_wall_down = (
            print_cross(flag_wall_right, flag_wall_down))

        if flag_wall_right:
            move_to_wall_left()
            if flag_wall_down:
                move_up()
                break
            move_down(4)
            print_cross()
        move_right(4)
        flag_wall_right = False


if __name__ == '__main__':
    run_tasks()
