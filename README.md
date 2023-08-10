# nyt-suite-solver
quick & small scripts to solve nyt mini games

solves [nyt spelling bee](https://www.nytimes.com/puzzles/spelling-bee) & [nyt letter boxed](https://www.nytimes.com/puzzles/letter-boxed)

## spellingbee.py

Usage:

For a game with centre letter k & surrounding letters p,e,s,y,n,a

`python spellingbee.py -f words.txt -l pKesyna`


f -> path to words.txt

l -> centre char in CAPS, surrounding chars in lowercase. order doesn't matter

Sample Output:

akenes
apeak
apeek
...
yanks
pangram count: 0
total words: 73
elapsed time: 0.011486s

## letterboxed.py

Usage: 

For a game with y,s,e r,i,o v,f,q d,u,t

`python letterboxed.py -f dedup.txt -l dut -r rio -t yse -b vfq`

f -> path to dedup.txt

l -> chars on left
r -> chars on right
t -> chars on top
b -> chars on bottom

Sample Output:

no one word solutions

two word solutions:
quito -> overdiversify
quoted -> diversify
