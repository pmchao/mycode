import pytest
from your_script_name import check_value, ValueTooSmallError, ValueTooLargeError

def test_value_too_large():
    with pytest.raises(ValueTooSmallError) as exc_info:
        check_value(105)  # Assuming 10 is the minimum acceptable value

    assert str(exc_info.value) == "The value 105 is too small."