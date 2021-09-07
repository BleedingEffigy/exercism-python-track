EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    '''
    :param layers: int number of layers in recipe

    Function that takes the number of layers used, and returns the total
    preparation time
    '''
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    :number_of_layers: int number of layers used
    :elapsed_bake_time: int amount of time elapsed

    Return amount of time elapsed
    '''
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
