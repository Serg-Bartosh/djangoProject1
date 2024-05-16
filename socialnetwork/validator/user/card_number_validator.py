from rest_framework.exceptions import ValidationError


def card_number_validator(card_number: str):
    if len(card_number.strip()) != 16:
        return ValidationError("Card number must be 16 characters long.")
