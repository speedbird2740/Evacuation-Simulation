import utils


class Person:
    ID = utils.get_id()

    def __init__(self, walk_speed):
        self.travel_speed = walk_speed

    # More code will be written (eventually)
