"""ACU CSE 101: Week 13 Practice - Inheritance and Polymorphism.

Think Python: Chapter 18
"""

import random


class Card:
    """Represents a standard playing card."""

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [
        None,
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self, suit: int = 0, rank: int = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"

    def __lt__(self, other: "Card") -> bool:
        # Compare suits first, then ranks
        t1 = (self.suit, self.rank)
        t2 = (other.suit, other.rank)
        return t1 < t2

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return (self.suit, self.rank) == (other.suit, other.rank)


class Deck:
    """Represents a deck of 52 cards."""

    def __init__(self):
        self.cards: list[Card] = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self) -> str:
        return "\n".join(str(card) for card in self.cards)

    def pop_card(self, i: int = -1) -> Card:
        """Remove and return a card from the deck."""
        return self.cards.pop(i)

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def shuffle(self) -> None:
        """Shuffle the deck in-place."""
        random.shuffle(self.cards)

    def move_cards(self, hand: "Hand", num: int) -> None:
        """Move num cards from deck into hand."""
        for _ in range(num):
            if self.cards:
                hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards held by a player (inherits from Deck)."""

    def __init__(self, label: str = ""):
        self.cards: list[Card] = []
        self.label = label
