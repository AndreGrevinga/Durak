import random
class Table:
    def __init__(self, numberOfPlayers):
        self.players = []
        self.numberOfPlayers = numberOfPlayers
        for eachNumber in range(numberOfPlayers):
            self.players.append(Player(eachNumber))
        self.deck = Deck()
        theTrumpCard = self.drawTrumpCard()
        self.trumpSuit = theTrumpCard.suit()
    def areNeighbours(self, firstPlayer, secondPlayer):
        isNormalNeighbour = abs(firstPlayer.number - secondPlayer.number) == 1
        isFirstAndLast = firstPlayer.number + secondPlayer.number == (self.numberOfPlayers - 1)
        return isNormalNeighbour or isFirstAndLast
    def drawUpToSixCards(self, player):
        while player.numberOfCards() < 6:
            player.playerHand.addCard(self.drawCardFromDeck())
    def drawCardFromDeck(self):
        return self.deck.drawCard()
    def shuffleDeck(self):
        self.deck.shuffle()
    def issueCards(self):
        for player in self.players:
            self.drawUpToSixCards(player)
class Player:
    def __init__(self, aNumber):
        self.number = aNumber
        self.playerHand = Hand()
    def numberOfCards(self):
        return self.playerHand.numberOfCards()
class Deck:
    def __init__(self):
        cards = []
        for suit in Card.suits:
            for number in Card.numbers:
                cards.append(Card(suit, number))
        self.remainingDeck = cards
    def drawTrumpCard(self):
        theCard = self.drawCard()
        self.remainingDeck.remove(theCard)
        self.trumpCard = theCard
        return theCard
    def drawCard(self):
        theCard = self.remainingDeck[0]
        self.remainingDeck.remove(theCard)
        return theCard
    def printDeck(self):
        for card in self.remainingDeck:
            card.printCard()
    def shuffle(self):
        random.shuffle(self.remainingDeck)
class Hand:
    def __init__(self):
        self.cards = []
    def numberOfCards(self):
        return len(self.cards)
    def addCard(self, aCard):
        self.cards.append(aCard)
class Card:
    suits = ['clubs ', 'diamonds ', 'hearts', 'spades']
    numbers = ['6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    def __init__(self, aSuit, aNumber):
        self.suit = aSuit
        self.number = aNumber
    @property
    def suit(self):
        return self.__suit
    def printCard(self):
        print(self.suit + ' ' + self.number)
class Rules:
    def __init__(self):
        self.enableShoving = False
def main():
    table = Table(2)
    table.shuffleDeck()
    table.issueCards()
    table.deck.printDeck()
if __name__ == "__main__":
    main()
