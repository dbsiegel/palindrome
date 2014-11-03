# #!/usr/bin/env python
# author: Deborah Siegel
# https://github.com/d3borah/palindrome

import re
from math import floor
from argparse import ArgumentParser

#parse arguments
def parse_cli_args ():
    parser = ArgumentParser(prog="palindrome detector", add_help=True,
                    description="palindrome detector...",
                    usage="palindromeDetector.py -input")

    parser.add_argument("input", nargs=1,
                   help='the word or phrase to check')
                   
    return parser.parse_args()


class MyText(object):
	@staticmethod   
	#compare putative mirror letters
	def palindrome_detect(phrase):
		print "checking the word or phrase: %s" % phrase
		letters = re.sub('[^a-z0-9\-\_]','',phrase.strip(' ').lower())
		myLen = len(letters)
		if myLen <= 1:
			print phrase , ".......it's not a palindrome."
		else:
			mirror = int(floor(myLen/2))
			start = 0
			end = -1
			for x in range(start, mirror):
				print letters[start], ":", letters[end]
				if letters[start] == letters[end]:
					start += 1
					end -= 1
				else:
					print phrase,".......it's not a palindrome."
					return
			print phrase,".......it's a palindrome."

#main
if __name__ == "__main__":   
	#palindrome_detect("Egad, a base tone denotes a bad age")
	args = parse_cli_args()    
	input = args.input[0]	 
	thing = MyText.palindrome_detect(input)
