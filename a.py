#
# 2022.06.17.
#
# Created by 김성찬.
#

#
# 01 파이썬 데이터 모델
#

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
deck = FrenchDeck()

print(f'len of deck: {len(deck)}')
print(f'first element in deck: {deck[0]}')
print(f'last element of deck: {deck[-1]}')
print(f'random element of deck: {choice(deck)}')
print(f'slice of deck: {deck[12::13]}')
