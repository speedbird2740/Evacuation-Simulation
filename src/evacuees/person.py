import typing


class Person(typing.TypedDict):
    ID: str
    travel_speed: float
    injuries: dict[str, float] # {name: slowdown %}
    ttl: float

