import pytest

from src.cinema_entry import can_watch

def test_age_16_returns_true():
    age = 16 # Arrange
    result = can_watch(age) # Act
    assert result is True # Assert


@pytest.mark.parametrize(
    "age",
    [16, 17, 18, 100],  # 16 is the boundary: "16 or older" is allowed
)
def test_age_16_or_older_returns_true(age):
    result = can_watch(age)

    assert result is True

@pytest.mark.parametrize(
    "age",
    [0, 1, 15],  # 0 is the lowest valid age; 15 is just below the boundary
)

def test_age_below_16_returns_false(age):
    result = can_watch(age)
    assert result is False

def test_negative_age_raises_value_error():
    with pytest.raises(ValueError):
        can_watch(-1)

@pytest.mark.parametrize(
    "invalid_value",
    ["16", 16.0, None, True, False],
)
def test_invalid_data_type_raises_type_error(invalid_value):
    with pytest.raises(TypeError):
        can_watch(invalid_value)

#demo1