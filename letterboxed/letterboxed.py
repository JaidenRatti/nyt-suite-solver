import argparse

def elim_invalid(filename,combined,assoc):
    with open(filename) as file:
        for_use = sorted(set(list(words.strip().lower() for words in file)))
        #keeping only possible words based on chars
        reduce = [word for word in for_use if set(word)-combined==set()]
        #ensure no letters from same side are adjacent
        #use the dictionary (pos) and check whether sides are the same for adjacent letters
        garbage = []
        for word in reduce:
            chars = list(word)
            valid = True
            for num in range(1,len(chars)):
                if assoc[chars[num]] == assoc[chars[num - 1]]:
                    valid = False
                    break
            if not valid:
                garbage.append(word)
        return [word for word in reduce if word not in garbage]

def one_word(key_list,characters):
    return [word for word in key_list if set(word) == characters]

def two_words(key_list,characters):
    result = []
    for word in key_list:
        last = word[-1]
        start_same_last = [second for second in key_list if second[0] == last and second != word]
        for w in start_same_last:
            duo = word + w
            if set(duo) == characters:
                result.append([word,w])
    return result

def main():
    ar = argparse.ArgumentParser()
    ar.add_argument('-f', '--words_file',required=True,help='input path to list of words')
    ar.add_argument('-l', '--left', required=True)
    ar.add_argument('-r','--right', required=True)
    ar.add_argument('-t','--top', required=True)
    ar.add_argument('-b','--bottom',required=True)
    args = ar.parse_args()
    
    left = dict((s.lower(), 'left') for s in args.left)
    right = dict((s.lower(), 'right') for s in args.right)
    top = dict((s.lower(), 'top') for s in args.top)
    bottom = dict((s.lower(), 'bottom') for s in args.bottom)
    assoc = {**left, **right, **top, **bottom}
    
    combined = set(assoc.keys())

    key_list = elim_invalid(args.words_file, combined,assoc)
    one_word_sols = one_word(key_list,combined)
    if not one_word_sols:
        print("no one word solutions")
    else:
        print("one word solutions:")
        print(one_word_sols)
    two_word_sols = two_words(key_list,combined)
    if not two_word_sols:
        print("no two word solutions")
    else:
        print("\ntwo word solutions:")
        for inner in two_word_sols:
            print(inner[0], "->",inner[1])

if __name__ == "__main__":
    main()