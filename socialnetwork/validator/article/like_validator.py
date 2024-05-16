def validate_like(value):
    print(value)
    if value is None or not isinstance(value, bool):
        return False
    return True
