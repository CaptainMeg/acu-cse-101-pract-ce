"""ACU CSE 101 - Automated Unit Tests for Week 13 Practice."""

from exercises.week_13_inheritance.practice import Card, Deck, Hand


def test_card_creation_str():
    c = Card(2, 11)  # Jack of Hearts
    assert str(c) == "Jack of Hearts"
    assert Card(0, 1) < Card(1, 1)  # Clubs < Diamonds


def test_deck_count():
    deck = Deck()
    assert len(deck.cards) == 52
    c = deck.pop_card()
    assert isinstance(c, Card)
    assert len(deck.cards) == 51


def test_hand_deal():
    deck = Deck()
    hand = Hand("Alice")
    deck.move_cards(hand, 5)
    assert len(hand.cards) == 5
    assert len(deck.cards) == 47
    assert hand.label == "Alice"
