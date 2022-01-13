import random


def get_id(chars: int = 6) -> str:
    id = ""
    charlist = list("1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")

    while not chars == 0:
        id += random.choice(charlist)

    return id