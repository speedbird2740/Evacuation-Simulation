import utils
import errors

class Walkway:
    ID = utils.get_id()

    def __init__(self, length: float, max_people: int, is_blocked: bool):
        self.length = length
        self.CAPACITY = max_people
        self.people = []
        self.is_blocked = is_blocked

    async def add_person(self, person):
        if len(self.people) >= self.CAPACITY:
            raise errors.WalkwayFull

        # More code in development


class Room:
    ID = utils.get_id()

    def __init__(self, max_people: int, is_blocked: bool):
        self.max_people = max_people
        self.people = []
        self.is_blocked = is_blocked
