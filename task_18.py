#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():

    def exit_from_labyrinth():
        while wall_is_above():
            if wall_is_on_the_left():
                while wall_is_above():
                    move_right()
                break
            move_left()

    exit_from_labyrinth()
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
