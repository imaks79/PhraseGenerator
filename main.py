import os

from numba import njit, jit

from utils import getmsg
from crypt import start_proc



# @jit(parallel = True)
def main():
	btc_path = os.path.join('data','btc.txt'); 
	eng_path = os.path.join('data', 'english.txt');

	add_set = set();
	nums = {};
	wordlist = [];

  	# ПОЛУЧЕНИЕ КОНСОЛЬНОЙ ИНФОРМАЦИИ   
	getmsg();


	with open(btc_path) as f:
		for line in f: 
			if line.strip(): 
				add_set.add(line.strip());
              
              
	with open(eng_path, 'r') as f:
		words = f.read().splitlines();
		i = 0;
		for word in f:
			nums[word.strip()] = i;
			wordlist.append(word.strip());
			i += 1;

	
	start_proc(add_set, words, nums, wordlist);


if __name__ == "__main__":
	main();