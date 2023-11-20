#Takes in the known variables and solves for unknown. If all are known, that is reported. 
def Force(force: float, mass: float, acceleration: float) -> float:
    if not force:
        return f'has a force of {mass * acceleration}'
    elif not mass:
        return f'has a mass of {force / acceleration}'
    elif not acceleration:
        return f'has an acceleration of {force / mass}'
    else:
        return 'All variables known'