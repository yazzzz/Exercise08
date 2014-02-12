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



def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #get random key from dictionary and add it to list
    random_key = (random.sample(chains.keys(), 1))
    sentence = [random_key[0][0],random_key[0][1]]
    while chains.get(random_key[0]): #while our key exists in the dict
        pick_value = chains[random_key[0]][random.randint(0, len(chains[random_key[0]])-1)]
        #make new bigram with y value from random_key and pick_value
        #print pick_value
        sentence.append(pick_value)
        random_key = [(random_key[0][1], pick_value)]
        #print random_key
        #print random_key[0]
        
        #new_bigram = y, pick_value
        #append new bigram to list
        #set new bigram to random_key so we can loop?    

    print "\n" +  " ".join(sentence)
   

    #write a while loop that says while i have valid key in dictionary, do this

    #while BLAH in chains.get():
    #use (x, y) key to pick random value. (y, value) becomes next key to print.    




    # for key, value in chains.iteritems():
    #     #print "%r : %r" % (key, value)
    #     #If there is only one value to choose from, choose that value.
    #     if len(value) == 1:
    #         # print key, value
    #         nextvalue = value
    #         #print key, nextvalue
    #     else:
    #     #If there are multiple values, pick a random value.    
    #         nextvalue = value[random.randint(0,len(value)-1)]
    #         #print key, nextvalue

    #     # To chain off this value, check dict to see if it's a key.

    #    # if nextvalue in [x for (x,y) in chains.keys()]:
    #     for (x, y) in chains.keys():
    #         if nextvalue == x:
    #             #print x, y
    #             markov_sentence = markov_sentence + " " + x + " " + y
    #             break
    # print markov_sentence    
            


    

def main():
    #args = sys.argv[1]
    script, filename  = sys.argv   
    # Change this to read input_text from a file
    f = open(filename)
    input_text = f.read()
    #print input_text

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()