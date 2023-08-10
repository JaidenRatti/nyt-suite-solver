def consec(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False

def filter(input_file, output_file):
    with open(input_file,'r') as inputfile, open(output_file, 'w') as outputfile:
        for line in inputfile:
            word = line.strip()
            if not consec(word):
                outputfile.write(word + '\n')


input_file = 'words.txt'
output_file = 'dedup.txt'

filter(input_file,output_file)
