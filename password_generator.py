from string import ascii_letters, digits
from random import sample

chars = ascii_letters + digits + '!@#$%^&*_'

def generate_password(length=24):
    return ''.join(sample(chars, length))