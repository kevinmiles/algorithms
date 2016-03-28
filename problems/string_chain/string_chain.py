# string_chain.py

import os
import sys


class Solution(object):

    def longest_chain(self, words):

        # sort words by word length and create a set
        words.sort(lambda x, y: cmp(len(x), len(y)))
        words_set = set(words)

        # chain_lengths[word] is the maximum length of a chain starting at word.
        # for each word, enumerate all words formed by removing one character and
        # see if such a word exists in the library. If it does, update chain_lengths
        # if a longer chain is formed by connecting to this word.
        # In the process, keep track of the global max_chain_length seen so far.
        chain_lengths = {}
        max_chain_length = 1
        for word in words:
            chain_lengths[word] = 1
            for i in xrange(len(word)):
                shorter_word = word[:i] + word[i+1:]
                if shorter_word in words_set:
                    chain_lengths[word] = max(chain_lengths[word], chain_lengths[shorter_word] + 1)
                    max_chain_length = max(max_chain_length, chain_lengths[word])

        return max_chain_length

    def main(self):
        _w_cnt = 0
        _w_cnt = int(input())
        _w_i=0
        _w = []
        while _w_i < _w_cnt:
            _w_item = input()
            _w.append(_w_item)
            _w_i+=1
        result = self.longest_chain(_w);
        print(result)

if __name__ == "__main__":
    Solution().main()

