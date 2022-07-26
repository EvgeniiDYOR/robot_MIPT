#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    def snake_print():
        while True:
            if wall_is_on_the_left():
                move_down(2)
                if wall_is_beneath():
                    move_up()
                    move_right()
                    break
                move_up()
                move_right()
            fill_cell()
            move_right()
            if wall_is_on_the_right():
                move_down()
                move_left()
                while True:
                    fill_cell()
                    move_left()
                    if wall_is_on_the_left():
                        break

    move_right()
    snake_print()


if __name__ == '__main__':
    run_tasks()
