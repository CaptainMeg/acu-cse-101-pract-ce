"""ACU CSE 101: Week 02 Practice - Variables, Expressions and Statements.

Think Python: Chapter 2
"""


def calculate_bookstore_cost(num_books: int) -> float:
    """Calculate the total wholesale cost for num_books.

    - Cover price: $24.95 with 40% bookstore discount.
    - Shipping: $3.00 for the first copy and $0.75 for each additional copy.
    """
    if num_books <= 0:
        return 0.0

    discounted_price_per_book = 24.95 * 0.60
    total_book_cost = num_books * discounted_price_per_book

    shipping_cost = 3.00 + (num_books - 1) * 0.75
    return round(total_book_cost + shipping_cost, 2)


def calculate_arrival_time(
    start_hour: int, start_min: int, easy_miles: float, tempo_miles: float
) -> tuple[int, int]:
    """Calculate arrival time given start time and running paces.

    - Easy pace: 8 min 15 sec (495 sec) per mile.
    - Tempo pace: 7 min 12 sec (432 sec) per mile.
    Returns (arrival_hour, arrival_min).
    """
    start_total_sec = (start_hour * 3600) + (start_min * 60)
    run_seconds = (easy_miles * 495) + (tempo_miles * 432)
    end_total_sec = start_total_sec + run_seconds

    arrival_hour = int(end_total_sec // 3600) % 24
    arrival_min = int((end_total_sec % 3600) // 60)
    return arrival_hour, arrival_min


def format_user_banner(text: str, width: int, border_char: str = "*") -> str:
    """Center text inside a banner of specified width surrounded by border_char."""
    return text.center(width, border_char)
