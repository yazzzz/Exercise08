#!/usr/bin/env python

import sys
import pprint

def make_chains(text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    text_list = text.split()
    print text_list
    text_dict = {}

    for i in range(2,len(text_list)):
        if not text_dict.get(i):
            text_dict[text_list[i-2], text_list[i-1]] = [text_list[i]]
        
    pprint.pprint(text_dict)

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    pass

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