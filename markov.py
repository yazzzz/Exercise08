#!/usr/bin/env python

import sys
import pprint
import random

def make_chains(text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    text_list = text.split()
    #print text_list
    text_dict = {}

    for i in range(2,len(text_list)):
        bgram1 = text_list[i-2]
        bgram2 = text_list[i-1]
        value = text_list[i]
        if not text_dict.get((bgram1, bgram2)):
            text_dict[bgram1, bgram2] = [value]
        else:
            text_dict[bgram1, bgram2] += [value]
    #pprint.pprint(text_dict)
    return text_dict

def pick_first_random_key(chains):
    random_key = (random.sample(chains.keys(), 1))
    while not random_key[0][0].istitle():
        random_key = (random.sample(chains.keys(), 1))
    return random_key        


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #get random key from dictionary and add it to list
    random_key = pick_first_random_key(chains)
    sentence = [random_key[0][0],random_key[0][1]]

    while chains.get(random_key[0]): #while our key exists in the dict
        pick_value = chains[random_key[0]][random.randint(0, len(chains[random_key[0]])-1)]
        #make new bigram with y value from random_key and pick_value
        sentence.append(pick_value)
        random_key = [(random_key[0][1], pick_value)]
        if len(" ".join(sentence)) <= 140:
            result =  "\n" +  " ".join(sentence)
        else:
            result =  "\n" +  "TOO LONG"
            break      
    return result
   

def main():
    #args = sys.argv[1]
    script, filename  = sys.argv 
    # Change this to read input_text from a file
    f = open(filename)
    input_text = f.read()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()