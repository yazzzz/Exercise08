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
    for key, value in chains.iteritems():
        #print "%r : %r" % (key, value)
        if len(value) == 1:
            print key, value
        else:
            print key, value[random.randint(0,len(value)-1)]

    

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