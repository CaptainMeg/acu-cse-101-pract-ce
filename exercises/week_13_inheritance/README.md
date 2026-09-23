# 📖 Week 13: Inheritance and Polymorphism
**Think Python**: Chapter 18

In this module, you will practice class inheritance, method overriding, and polymorphism using a standard deck of playing cards (`Card`, `Deck`, `Hand`).

---

## 🎯 Exercises

1. `Card(suit, rank)`:
   - Suit names: `['Clubs', 'Diamonds', 'Hearts', 'Spades']`.
   - Rank names: `[None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']`.
   - `__str__` and comparison operators (`<`, `==`).

2. `Deck`:
   - Contains a list of 52 `Card` objects.
   - Methods: `pop_card()`, `add_card(card)`, `shuffle()`, `deal_hands(num_hands, num_cards)`.

3. `Hand(Deck)`:
   - Inherits from `Deck`. Represents a player's hand with an assigned label (e.g. `'Player 1'`).
