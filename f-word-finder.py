import requests
import re
from itertools import permutations

def lambda_handler(event, context):
    alpha_ls = list(event['v1'])
    word_count = int(event['v2'])
    word_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    pattern = '<meta property="og:description" content='
    #cntr = 2
    cntr = word_count
    word_set = set()
    
    if len(alpha_ls) < word_count:
        return "Please enter equal or more alphabets than the word count you have entered."
        
    while cntr <= len(alpha_ls):
        perm = permutations(alpha_ls,cntr)
        for i in list(perm):
            word = ''
            for alphabet in i:
                word = word + alphabet
            url="https://www.merriam-webster.com/dictionary/" + word
            response = requests.get(url, headers=headers)
            result = re.search(pattern, response.text)
            if not result == None:
                word_set.add(word)
        cntr += 1
    word_list = list(word_set)
    word_list.sort()
    
    message = "Here are the useful words from the entered alphabets - " + str(word_list).strip('[').strip(']')
    print(message)
    return message