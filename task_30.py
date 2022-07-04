#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():

    def field_size():
        result = 1
        while wall_is_on_the_right() != True:
            move_right()
            result += 1
        while wall_is_on_the_left() != True:
            move_left()
        return result

    
    def triangle_right(size):
        for i in range(size):
            move_right()
            fill_cell()
        move_right()

    def triangle_down(size):
        for i in range(size):
            move_down()
            fill_cell()
        move_down()

    def triangle_left(size):
        for i in range(size):
            move_left()
            fill_cell()
        move_left()

    def triangle_up(size):
        for i in range(size):
            move_up()
            fill_cell()
        move_up()

    def finish():
        while wall_is_beneath() != True:
            move_down()
        while wall_is_on_the_left() != True:
            move_left()



    size = field_size() - 2
    while size > 0:
        triangle_right(size)
        triangle_down(size)
        triangle_left(size)
        triangle_up(size)
        move_right()
        move_down()
        size -= 2
    finish()




if __name__ == '__main__':
    run_tasks()
