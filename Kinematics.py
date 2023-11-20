def Force(force: float, mass: float, accleration: float) -> float:
    if not force:
        return mass * accleration
    elif not mass:
        return force / accleration
    elif not accleration:
        return force / mass