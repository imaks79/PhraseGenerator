from report import getmsg
from crypt import start_proc



def main():
	Address = os.path.join('data','btc.txt'); 
	
	add_set = set();
	nums = {}
	wordlist = []
	
	# ПОЛУЧЕНИЕ КОНСОЛЬНОЙ ИНФОРМАЦИИ   
	getmsg();
	
	
	with open(Address) as f:
	    for line in f:
	        if line.strip():
	            add_set.add(line.strip());
	            
	            
	with open(os.path.join('data', 'english.txt'), 'r') as f:
		words = f.read().splitlines();
        i = 0;
        for word in f:
            nums[word.strip()] = i;
            wordlist.append(word.strip());
            i += 1;
	            
	# ПОЛУЧЕНИЕ КОНСОЛЬНОЙ ИНФОРМАЦИИ            
	getmsg(add_set);
	
	# ########## ########## ########## ########## ##########
	# TODO: ОТПРАВЛЯЕМ В ПРОЦЕСС ЧЕТЫРЕ ЗНАЧЕНИЯ, С КОТОРЫМИ ДАЛЬШЕ ИДЕТ РАБОТА
	start_proc(add_set, words, nums, wordlist);
	#
	# ########## ########## ########## ########## ##########


if __name__ == "__main__":
	main();
	
