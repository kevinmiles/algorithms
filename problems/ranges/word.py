import itertools

w = open('/usr/share/dict/words', 'r')
dictionary = set(w.read().splitlines())
w.close()

def find_longest_word(word):
    for i in xrange(1, len(word)):
        combinations = itertools.combinations(range(len(word)), i)
        for combination in combinations:
            test_word = ''
            for j in xrange(len(word)):
                if j not in combination:
                    test_word += word[j]
            if test_word in dictionary:
                return test_word

print find_longest_word('yamnitsky')
