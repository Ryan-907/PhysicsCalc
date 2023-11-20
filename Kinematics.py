def Force(force: float, mass: float, accleration: float) -> float:
    if force is None:
        return mass * accleration
    elif mass is None:
        return force / accleration
    elif accleration is None:
        return force / mass
    