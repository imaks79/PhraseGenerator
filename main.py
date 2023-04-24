import os

# import pandas as pd
from numba import njit, jit

from utils import getmsg
from crypt import start_proc


BTC_PATH = os.path.join('data','btc.txt'); 
ENG_PATH = os.path.join('data', 'english.txt');


# @njit(parallel = True)
def main():


    add_set = set();
    nums = {};
    wordlist = [];

    # ПОЛУЧЕНИЕ КОНСОЛЬНОЙ ИНФОРМАЦИИ   
    getmsg();




    # TODO: Переделать под pandas
    # data = pd.read_csv(BTC_PATH, sep = " ", header = None)
    with open(BTC_PATH, 'r') as f:
        for line in f: 
            if line.strip(): 
                add_set.add(line.strip());
              
    # TODO: Переделать под pandas   
    # data = pd.read_csv(ENG_PATH, sep = " ", header = None)
    with open(ENG_PATH, 'r') as f:
        words = f.read().splitlines();

    with open(ENG_PATH, 'r') as f:	
        i = 0;
        for word in f:
            nums[word.strip()] = i;
            wordlist.append(word.strip());
            i += 1;



    start_proc(add_set, words, nums, wordlist);


if __name__ == "__main__":
    main();