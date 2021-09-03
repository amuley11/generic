import json

def lambda_handler(event, context):
    vs_num=event['v1'].replace(' ','')
    
    if not vs_num.isdigit():
        return "You entered - " + vs_num + ", which is not  an integer! Please enter a valid integer number."
    
    v_num = int(vs_num)
    d = [1] # List to hold the prime mumbers
    e = 2 # Starting point
    
    while e <= v_num:
        c = [] # List to hold the numbers by which entered number is divisible
        for b in range(2,e):
            if e % b == 0: # Check whether the number is divisible
                c.append(b) # Append it to the list "c" if it is divisible
                continue
        if len(c) == 0:
            d.append(e) # If this number is not divisble by any number then enter it to the list "d"
        e=e+1 # Go to the next number to repeat the activity
        
    return (f'List of prime numbers till {v_num} are - {d}')