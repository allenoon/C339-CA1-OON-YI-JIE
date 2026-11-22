import pytest

from src.cinema_price import ticket_price

def test_one_ticket_returns_1200():
    ticket_count = 1 # Arrange
    result = ticket_price(ticket_count) # Act
    assert result == 1200 # Assert

@pytest.mark.parametrize(
    "ticket_count, expected",
    [
        (0, 0),  # boundary: zero tickets costs zero
        (1, 1200),  # boundary: smallest purchase
        (2, 2400),
        (100, 120000),  # large valid value
    ],
)
def test_valid_ticket_count_returns_total_in_cents(ticket_count, expected):
    result = ticket_price(ticket_count)
    assert result == expected

def test_negative_ticket_count_raises_value_error():
    with pytest.raises(ValueError):
        ticket_price(-1)

@pytest.mark.parametrize(
    "invalid_value",
    ["3", 2.5, None, True, False],
)
def test_invalid_data_type_raises_type_error(invalid_value):
    with pytest.raises(TypeError):
        ticket_price(invalid_value)
        #demo