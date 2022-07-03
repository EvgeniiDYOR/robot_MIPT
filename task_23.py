#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():

    counter = 0
    flag = False
    
    def move_back(counter):
        while counter != 0:
            move_left()
            counter -= 1

    def print_up():
        while wall_is_above() != True:
            move_up()
            fill_cell()
        fill_cell()
    
    def move_to_wall_down():
        while wall_is_beneath() != True:
            move_down()
    
    while flag != True:
        move_right()
        counter += 1
        if wall_is_above() != True:
            print_up()
            move_to_wall_down()
        if wall_is_on_the_right() == True:
            move_back(counter)
            flag = True
            break



if __name__ == '__main__':
    run_tasks()
