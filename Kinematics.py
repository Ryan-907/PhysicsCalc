#Takes in the known variables and solves for unknown. If all are known, that is reported. 
def Force(force: float, mass: float, acceleration: float) -> float:
    if not force:
        return mass * acceleration
    elif not mass:
        return force / acceleration
    elif not acceleration:
        return force / mass
    else:
        return 'All variables known'
    
def Work(work: float, force: float, distance: float) -> float:
    if not work:
        return force * distance
    elif not force:
        return work/distance
    elif not distance:
        return work/force
    else:
        return 'All variables known'