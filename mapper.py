#!/usr/bin/env python

import sys
import re


def main(separator = '\t'):
	for line in sys.stdin:
		#replace all the special characters with spaces
	    word = re.sub(r'[^a-zA-Z0-9]', " ", line.strip())

	    #to split the line in to the list
	    word_list = word.split()

	    for i , k in enumerate(word_list):
	    	
	    	# check for the number of words in the line
	        if (i + 1) >= len(word_list):
	        
	            print ('%s%s%s' % (k, separator, 1))

	        else:
	        	
	        	print ('%s%s%s' % ((k + ' ' + word_list[i + 1]),separator, 1))
	            


if __name__ == "__main__":
    main()