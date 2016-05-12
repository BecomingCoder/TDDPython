def is_leap_year(self):
    if self == 1900:
        return False
    elif self % 4 == 0:
        return True
    else:
        return False
