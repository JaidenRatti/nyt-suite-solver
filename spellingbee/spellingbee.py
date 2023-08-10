import argparse
import time

def find_centre(letters):
    centre = None
    surrounding = ""
    for char in letters:
        if char.isupper() and not centre:
            centre = char.lower()
        else:
            surrounding += char.lower()
    return centre, surrounding

def valid(words, centre, surrounding):
    valid = set(centre + surrounding)
    return all(l in valid for l in words)

def valid_centre(path, centre, surrounding):
    final = []
    pangram = 0
    with open(path, 'r') as file:
        for word in file.read().split():
            if centre in word and len(word) >= 4 and valid(word, centre, surrounding):
                final.append(word)
                if all(l in word for l in surrounding):
                    pangram += 1
    return final, pangram

def main():      
    ar = argparse.ArgumentParser()
    ar.add_argument('-f', '--words_file',required=True, help='input path to list of words')
    ar.add_argument('-l', '--letters',required=True,help="input letters (no spaces or commas), where centre letter is CAPS and rest are lowercase")
    #i.e -f words.txt -l pKesyna
    args = ar.parse_args()

    start = time.time()
    centre,surrounding= find_centre(args.letters)
    answers,pangram = valid_centre(args.words_file,centre,surrounding)

    for word in answers:
        print(word)

    print(f"pangram count: {pangram}")
    print(f"total words: {len(answers)}")
        
    end = time.time()    
    elapsed = end - start
    print(f"elapsed time: {elapsed:4f}s")
    
if __name__ == "__main__":
    main()
