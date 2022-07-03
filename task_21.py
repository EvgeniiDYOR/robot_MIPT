#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():

    def print(x):
        for i in range(x):
            move_right() 
            fill_cell() 
        for i in range(x):   
            move_left()
        move_down()

    move_down()
    for i in range(13):
        print(i+1)
    move_right()
    




if __name__ == '__main__':
    run_tasks()
