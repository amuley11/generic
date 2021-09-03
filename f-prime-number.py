import json

def lambda_handler(event, context):
    vs_num=event['v1'].replace(' ','')
    
    if not vs_num.isdigit():
        return "You entered - " + vs_num + ", which is not  an integer! Please enter a valid integer number."
    
    v_num = int(vs_num)
        
    c=[] # Setting up an empty list to collect numbers
    
    for b in range(2,v_num):
        if v_num % b == 0: # Check whether the number is divisible
            c.append(b) # Append it to the list "c" if it is divisible
            continue

    if len(c) == 0:
        return (f'{v_num} is a prime number')
    else:
        return (f'{v_num} is not a prime number as it is divisible by {c}')