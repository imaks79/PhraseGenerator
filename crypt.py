import os, time, random
from numba import njit, jit


from utils import isOk


from bip_utils import (
    Bip39MnemonicGenerator, Bip39MnemonicDecoder, Bip39SeedGenerator,
    Bip39WordsNum, Bip39Languages,
    Bip44, Bip44Coins, Bip44Changes,
    Bip49, Bip49Coins,
    Bip84, Bip84Coins,
    Bip86, Bip86Coins,
    Bip32Slip10Secp256k1, EthAddrEncoder
)


# @njit(parallel = True)
@jit(parallel = True)
def start_proc(add_set:set, __words__:list, __nums__:dict, __wordlist__:list):
	'''
	add_set => <class 'set'>
	words => <class 'list'>
	nums => <class 'dict'>
	wordlist => <class 'list'>
	'''
	
	while True:
		
		words, nums, wordlist = __words__, __nums__, __wordlist__;

		ddd = ' '.join(random.sample(words, 11));

		# ddd = "between cage ketchup write supreme cash destroy shy escape nothing wild"
		words = [w.lower() for w in ddd.split() if w.lower() in nums];

		start_time = time.time();
		generated_results_count = 0;

		if len(words) == 11:
			for i in range(2048):
				cand = words + [wordlist[i]];
				result = ' '.join(cand);
				# ######## ######## ######## ######## # 
				generated_results_count += 1;
				if generated_results_count % 100 == 0:
					elapsed_time = time.time() - start_time;
					results_per_second = generated_results_count // elapsed_time;
					print(f"{generated_results_count} полученные результаты ({results_per_second} SEED/second)", end = '\r', flush = True);
				# ######## ######## ######## ######## #
		        if isOk(cand, nums):
		            seed_bytes = Bip39SeedGenerator(result).Generate();
		            bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN);
		            # bip49_mst_ctx = Bip49.FromSeed(seed_bytes, Bip49Coins.BITCOIN);
		            # bip84_mst_ctx = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN);
		            # bip86_mst_ctx = Bip86.FromSeed(seed_bytes, Bip86Coins.BITCOIN);
		            bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0);
		            # bip49_acc_ctx = bip49_mst_ctx.Purpose().Coin().Account(0);
		            # bip84_acc_ctx = bip84_mst_ctx.Purpose().Coin().Account(0);
		            # bip86_acc_ctx = bip86_mst_ctx.Purpose().Coin().Account(0);
		            bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT);
		            # bip49_chg_ctx = bip49_acc_ctx.Change(Bip44Changes.CHAIN_EXT);
		            # bip84_chg_ctx = bip84_acc_ctx.Change(Bip44Changes.CHAIN_EXT);
		            # bip86_chg_ctx = bip86_acc_ctx.Change(Bip44Changes.CHAIN_EXT);
		            print(result);
		            for i in range(20):
		                # bip32_der_ctx = bip32_mst_eth.DerivePath("m/44'/60'/0'/0/" + str(i))
		                bip44_addr_ctx = bip44_chg_ctx.AddressIndex(i);
		                seed44 = bip44_addr_ctx.PublicKey().ToAddress();
		                # bip49_addr_ctx = bip49_chg_ctx.AddressIndex(i);
		                # seed49 = bip49_addr_ctx.PublicKey().ToAddress();
		                # bip84_addr_ctx = bip84_chg_ctx.AddressIndex(i);
		                # seed84 = bip84_addr_ctx.PublicKey().ToAddress();
		                # bip86_addr_ctx = bip86_chg_ctx.AddressIndex(i);
		                # seed86 = bip86_addr_ctx.PublicKey().ToAddress();
						# ######### ######### ######### ######### #########
		                # eth_addr = EthAddrEncoder.EncodeKey(bip32_der_ctx.PublicKey().KeyObject())
		                # eth = ((eth_addr) [2:]) # если ваши адреса ETH начинаются без 0x в начале
		                '''Раскоментировать стоку ниже, если ваши адреса ETH начинаются с 0x'''
		                # eth = ((eth_addr)) # если ваши адреса ETH начинаются c 0x в начале
		                
		                if seed44 in add_set or seed49 in add_set or seed84 in add_set or seed86 in add_set:
		                    print(result);
		                    d = open(f"seed.txt","a");
		                    d.write(str(result) + '\n' + str(seed44) + '\n'+ str(seed49) + '\n'+ str(seed84) + '\n'+ str(seed86) + '\n');
		                    d.flush();
		                    d.close();
		                elif len(words) == 12:
		                    print('OK' if isOk(words, nums) else 'Invalid', 'wordlist checksum');
