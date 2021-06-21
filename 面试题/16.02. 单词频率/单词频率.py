#!/usr/bin/python3

from typing import List


class WordsFrequency:

    def __init__(self, book: List[str]):
        self.d = dict()
        for b in book:
            self.d[b] = self.d.get(b, 0) + 1

    def get(self, word: str) -> int:
        return self.d.get(word, 0)


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
