import utils


class Person:
    ID = utils.get_id()

    def __init__(self, travel_speed: float = 3.5):
        self.travel_speed = travel_speed
