

def main():
  i = 0;
  nums = {};
  wordlist = [];
  add_set = set();
    
  with open('btc.txt') as f:
    for line in f:
      if line.strip():
        add_set.add(line.strip());
    
  with open('english.txt', 'r') as f:
    words = f.read().splitlines();
    for word in f:
      nums[word.strip()] = i;
      wordlist.append(word.strip());
      i += 1;
            
  print(f'add_set => {type(add_set)}');
  print(f'words => {type(words)}');
  print(f'nums => {type(nums)}');
  print(f'wordlist => {type(wordlist)}');


if __name__ == "__main__":
  main();
	
	
