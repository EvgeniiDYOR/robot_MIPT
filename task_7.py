#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    for i in range(15):
        counter = 0
        move_down()
        if wall_is_beneath() == True:
            while wall_is_beneath() == True:
                move_right()
                counter += 1
            move_down()
            move_left(counter)
            break



if __name__ == '__main__':
    run_tasks()
