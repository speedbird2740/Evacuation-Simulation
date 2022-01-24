import asyncio

import utils
import errors

from evacuees.person import Person


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

    async def simulate_smoke(self, intensity: int):
        if intensity > 5:
            raise Exception
        # smoke effects on evacuees to be determined

    async def simulate_fire(self, intensity: int):
        if intensity > 5:
            raise Exception
        # fire damage/effects on evacuees to be determined


class Room:

    def __init__(self, max_people: int, is_blocked: bool):
        self.max_people = max_people
        self.people = []
        self.is_blocked = is_blocked
        self.ID = utils.get_id()

    def add_person(self, count: int = 1, walk_speed: float = 3.5):
        if len(self.people) >= self.max_people or len(self.people) + count >= self.max_people:
            raise errors.RoomFull

        while count > 0:
            new_person = Person(walk_speed)
            self.people.append(new_person)
            count -= 1

    async def simulate_smoke(self, intensity: int):
        if intensity > 5:
            raise Exception
        # smoke effects on evacuees to be determined

    async def simulate_fire(self, intensity: int):
        if intensity > 5:
            raise Exception
        # fire damage/effects on evacuees to be determined
