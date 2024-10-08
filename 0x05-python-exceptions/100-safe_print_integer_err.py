#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=open('/dev/stderr', 'w'))
        return False
