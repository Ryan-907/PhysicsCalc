from dataclasses import dataclass

@dataclass
class material:
    name: str
    force: float
    mass: float
    acceleration: float
    weight: float
    distance: float
    time: int
    work: float