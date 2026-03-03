from app.input_validators import validate_number
from app.exceptions import ValidationError

def test_validate_number_valid():
    assert validate_number(10) == 10

def test_validate_number_invalid():
    with pytest.raises(ValidationError):
        validate_number("abc")