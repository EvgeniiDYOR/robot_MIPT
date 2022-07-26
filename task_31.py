#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():

    while True:
        flag_right, flag_left = False, False

        while not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                break
            if wall_is_on_the_right():
                flag_right = True

        while not wall_is_on_the_left():
            move_left()
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
                break
            if wall_is_on_the_left():
                flag_left = True

        if flag_right and flag_left:
            break


if __name__ == '__main__':
    run_tasks()
