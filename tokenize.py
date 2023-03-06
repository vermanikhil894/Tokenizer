import gzip, re, sys

def tokenize(l):
    return l.split()

fname = sys.argv[1]

with gzip.open(fname, mode='rt', encoding='utf-8') as infile:
    for line in infile:
        tokens = tokenize(line)
        for t in tokens:
            word = re.split(r"\$@?#?^[a-zA-Z]+[a-zA-Z0-9-_']*[a-zA-Z0-9]$ | [\s^\w\s]+", t)
            for ele in word:
                if ele.strip():
                    print(ele)
            print()
