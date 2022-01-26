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
        self.fire_intensity = 0
        self.travel_multiplier = 1
        self.auto_smoke = False

    async def cross(self, person):
        if self.people >= self.CAPACITY:
            raise errors.WalkwayFull

        self.people += 1
        travel_time = self.LENGTH / person.travel_speed

        while travel_time > 0:
            if travel_time >= 1:
                await asyncio.sleep(1 * self.travel_multiplier)
                travel_time -= 1
            else:
                await asyncio.sleep(travel_time * self.travel_multiplier)
                travel_time = 0

        self.people -= 1
        # More code in development

    async def simulate_smoke(self, multiplier: float = None, auto: bool = False):
        if multiplier > 6:
            raise Exception
        if multiplier and auto:
            raise Exception

        if auto:
            if self.auto_smoke:
                raise Exception
            self.auto_smoke = True

            while self.travel_multiplier < 6:
                self.travel_multiplier += 0.1
                await asyncio.sleep(2 / self.fire_intensity if self.fire_intensity > 0 else 1)
        else:
            self.travel_multiplier = multiplier

    async def simulate_fire(self, intensity: float):
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
