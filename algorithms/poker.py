
class Suit():
    heart = 1
    diamond = 2
    club = 3
    spade = 4

class Value():
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

class HandType():
    high = 1
    pair = 2
    twoPair = 3
    threeOfAKind = 4
    straight = 5
    flush = 6
    fullHouse = 7
    fourOfAKind = 8
    straightFlush = 9
    royalFlush = 10

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Hand():

    def __init__(self, cards):
        self.cards = cards

    def score(self):

        self.type = 0
        self.value1 = 0
        self.value2 = 0
        self.value3 = 0
        self.value4 = 0
        self.value5 = 0

        self.cards.sort(key=lambda c: c.value)
        values = {}
        for c in self.cards:
            if c.value in values:
                values[c.value] += 1
            else:
                values[c.value] = 1

        self.type = HandType.highCard
        self.value1 = self.cards[-1]
        self.value2 = self.cards[-2]
        self.value3 = self.cards[-3]
        self.value4 = self.cards[-4]
        self.value5 = self.cards[-5]

        # check for pair
        for value in values:
            if values[value] == 2:
                self.type = HandType.pair
                self.value1 = value
                remainingCards = [card for card in self.cards if card.value != value]
                self.value2 = remainingCards[-1]
                self.value3 = remainingCards[-2]
                self.value4 = remainingCards[-3]
                self.value5 = 0

        # check for two pair
        if self.type == HandType.pair:
            pair1 = self.value1
            for value in values:
                if values[value] == 2 and value != pair1:
                    pair2 = value
                    self.type = HandType.twoPair
                    self.value1 = max(pair1, pair2)
                    self.value2 = min(pair1, pair2)
                    self.value3 = [card for card in self.cards if card.value != self.value1 and card.value != self.value2][0].value
                    self.value4 = 0
                    self.value5 = 0

        # check for three of a kind
        for value in values:
            if values[value] == 3:
                self.type = HandType.threeOfAKind
                self.value1 = value

        # check for a straight
        found = True
        for i in xrange(1, len(self.cards)):
            if self.cards[i].value != self.cards[i-1].value + 1:
                found = False
        if found:
            self.type = HandType.straight
            self.value1 = self.cards[-1]
            self.value2 = self.cards[-2]

        # check for a flush
        if len(set(card.suit for card in self.cards)) == 1:
            self.type = HandType.flush
            self.value1 = self.cards[-1]
            self.value2 = self.cards[-2]

        # check for a full house
        if self.type == HandType.threeOfAKind:
            for value in values:
                if values[value] == 2:
                    self.type = HandType.fullHouse
                self.value2 = value

        return (self.type, self.value1, self.value2)

    # returns -1 if self is stronger, 0 if equal, 1 if other is stronger
    def compare(self, other):
        return cmp(self.score(), other.score())

hand1 = Hand([
    Card(Suit.spade, Value.two),
    Card(Suit.heart, Value.two),
    Card(Suit.diamond, Value.four),
    Card(Suit.club, Value.five),
    Card(Suit.spade, Value.five),
])

print hand1.score()

