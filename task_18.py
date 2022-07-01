#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():

    def exit():
        while wall_is_on_the_left() != True:
            move_left()
            if wall_is_above() != True:
                break
            elif wall_is_beneath() != True:
                break 
        if wall_is_on_the_left() == True:
            while wall_is_on_the_right() != True:
                move_right()
                if wall_is_above() != True:
                    break
                elif wall_is_beneath() != True:
                    break
   

    def move_to_wall_left():
        while wall_is_on_the_left() != True:
            move_left() 
    
    def move_to_wall_right():
        while wall_is_on_the_right() != True:
            move_right()

    def move_to_wall_up():
        while wall_is_above() != True:
            move_up()
    
    def move_to_wall_down():
        while wall_is_beneath() != True:
            move_down()


    exit()
    if wall_is_above() != True:
        move_to_wall_up()
        move_to_wall_left()
    elif wall_is_beneath() != True:
        move_to_wall_down()
        move_to_wall_left()
        move_to_wall_up()





if __name__ == '__main__':
    run_tasks()
