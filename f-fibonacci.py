import json
import os

def show_fibonacci(event, context):
    num_position=int(event['v1'].replace(' ',''))
    '''
    This is a function to generate a fibonacci series till the position entered by the user
    '''
    fibonacci_list = []
    counter = 2
    
    while len(fibonacci_list) < num_position:
        if counter == 2:
            fibonacci_list.append(0)
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        counter += 1

    response = 'Fibonacci series till position ' + str(num_position) + " - " + str(fibonacci_list).strip('[]')
    print(response)
    return response