import asyncio

import utils
import errors


class Walkway:

    def __init__(self, length: float, max_people: int, is_blocked: bool):
        self.LENGTH = length
        self.CAPACITY = max_people
        self.people = 0
        self.is_blocked = is_blocked
        self.ID = utils.get_id()

    async def cross(self, person):
        if self.people >= self.CAPACITY:
            raise errors.WalkwayFull

        self.people += 1
        travel_time = self.LENGTH / person.travel_speed

        await asyncio.sleep(travel_time)

        self.people -= 1
        # More code in development


class Room:

    def __init__(self, max_people: int, is_blocked: bool):
        self.max_people = max_people
        self.people = []
        self.is_blocked = is_blocked
        self.ID = utils.get_id()
