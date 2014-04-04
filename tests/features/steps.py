from lettuce import *

@step('I have a number (\d+)')
def have_a_number(step, number):
    world.number = int(number)