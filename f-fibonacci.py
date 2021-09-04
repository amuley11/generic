import json
import os

def show_fibonacci(event, context):
    num_position=int(event['v1'].replace(' ',''))
    '''
    This is a function to generate a fibonacci series till the position entered by the user
    '''
    fibonacci_list = []

    while len(fibonacci_list) < num_position:
        if len(fibonacci_list) < 1:
            fibonacci_list.append(0)
        elif len(fibonacci_list) < 2:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    if num_position == 0:
        response = "Since you have entered 0, fibonacci series couldn't be generated."
    else:
        response = 'Fibonacci series till position ' + str(num_position) + " - " + str(fibonacci_list).strip('[]')
    
    print(response)
    return response
