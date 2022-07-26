#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():

    flag = False
    
    def print_cross(flag_):
        for i in range(2):
            fill_cell()
            move_right()
            fill_cell()
            if wall_is_on_the_right():
                flag_ = True
        move_left()
        move_up()
        fill_cell()
        move_down(2)
        fill_cell()
        return flag_

    move_down(2)
    while not flag:
        flag = print_cross(flag)
        if flag:
            move_left()
            move_up(2)
            break
        move_right(3)
        move_up()


    



if __name__ == '__main__':
    run_tasks()
