import asyncio
import time

import utils
import errors

from evacuees.person import Person


class Walkway:

    def __init__(self, length: float, max_people: int, is_blocked: bool, is_exit: bool = False):
        self.LENGTH = length
        self.CAPACITY = max_people
        self.people = 0
        self.is_blocked = is_blocked
        self.ID = utils.get_id()
        self.fire_intensity = 0
        self.travel_multiplier = 1
        self.auto_smoke = False
        self.auto_fire = False

    async def cross(self, person):
        if self.people >= self.CAPACITY:
            raise errors.WalkwayFull

        self.people += 1
        travel_time = self.LENGTH / person.travel_speed

        while travel_time > 0:
            if travel_time >= 1:
                await asyncio.sleep(1 * self.travel_multiplier)
                person.ttl -= 1 * self.travel_multiplier
                travel_time -= 1
            else:
                await asyncio.sleep(travel_time * self.travel_multiplier)
                person.ttl -= travel_time * self.travel_multiplier
                travel_time = 0

            if person.ttl <= 0:
                raise Exception

        self.people -= 1

        return person
        # More code in development

    async def simulate_smoke(self, intensity: float, auto: bool):
        # Smoke damage/effects to be determined
        if intensity > 5:
            raise Exception
        elif intensity and auto:
            raise Exception

        if auto:
            if self.auto_smoke:
                raise Exception
            self.auto_smoke = True

            while self.travel_multiplier < 5:
                self.travel_multiplier += 0.1
                await asyncio.sleep(2 / self.fire_intensity if self.fire_intensity > 0 else 1)
        else:
            self.travel_multiplier = intensity

    async def simulate_fire(self, intensity: float, auto: bool):
        if intensity > 5:
            raise Exception

        if auto:
            if self.auto_fire:
                raise Exception

            while self.fire_intensity < 5:
                self.fire_intensity += 0.1
                await asyncio.sleep(2 / intensity if intensity > 0 else 1)
        else:
            self.fire_intensity = intensity


class Room:

    def __init__(self, max_people: int, is_blocked: bool):
        self.max_people = max_people
        self.people = {}
        self.is_blocked = is_blocked
        self.ID = utils.get_id()
        self.fire_intensity = 0
        self.travel_multiplier = 1
        self.auto_smoke = False
        self.auto_fire = False

    def add_person(self, count: int, walk_speed: float):
        if len(self.people) >= self.max_people or len(self.people) + count >= self.max_people:
            raise errors.RoomFull

        while count > 0:
            new_person = Person(walk_speed, ID=utils.get_id())
            self.people[new_person.ID] = new_person
            count -= 1

    async def simulate_smoke(self, intensity: int, auto: bool):
        # Smoke damage/effects to be determined
        if intensity > 5:
            raise Exception
        elif intensity and auto:
            raise Exception

        if auto:
            if self.auto_smoke:
                raise Exception
            self.auto_smoke = True

            while self.travel_multiplier < 5:
                self.travel_multiplier += 0.1
                await asyncio.sleep(2 / self.fire_intensity if self.fire_intensity > 0 else 1)
        else:
            self.travel_multiplier = intensity

    async def simulate_fire(self, intensity: int, auto: bool):
        if intensity > 5:
            raise Exception

        if auto:
            if self.auto_fire:
                raise Exception

            while self.fire_intensity < 5:
                self.fire_intensity += 0.1
                await asyncio.sleep(2 / intensity if intensity > 0 else 1)
        else:
            self.fire_intensity = intensity
