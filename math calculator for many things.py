import math
mode = input("What would you like to compute? (quad, trig)" '\n')

# Quadratics section

if mode == "quad":

    # Code for finding the roots of a quadratic equation. Considering its literally just the quadratic formula, it wasn't too difficult to make

    quadmode = input("What part of the quadratic would you like to compute? (roots, abc)" '\n')
    print("NOTICE: this code cannot compute complex numbers." '\n')
    if quadmode == "roots":
        aVal = float(input("What is your a value?" '\n'))
        bVal = float(input("What is your b value?" '\n'))
        cVal = float(input("What is your c value?" '\n'))
        disc = (bVal ** 2) - (4 * aVal * cVal)
        # had to make the discriminant its own variable, code was getting too cluttered
        quadroot1 = (0 - bVal + math.sqrt(disc)) / (2 * aVal)
        quadroot2 = (0 - bVal - math.sqrt(disc)) / (2 * aVal)
        print("disc is", disc, ",root 1 is", float(quadroot1), ",and root 2 is", float(quadroot2))

    # Code for finding abc values of a quadratic equation in standard form. It kinda sucks, i'll improve it later.

    elif quadmode == "abc":
        print("NOTICE: i dont actually know if this code is accurate... so just factor, dummy.")
        abcroot1 = float(input("What is your first root?" '\n'))
        abcroot2 = float(input("What is your second root?" '\n'))
        aVal = float(input("What is your a value?" '\n'))
        cVal = (abcroot1 * abcroot2) * aVal
        bVal = -((abcroot1 + abcroot2) * aVal)
        print("aVal is", aVal, ", bVal is", bVal, ", cVal is", cVal, ".")
    else:
        print("That isn't a function of this calculator.")

# Trigonometry section

if mode == "trig":
    trigmode = input("What kind of trig would you like to compute? (angle, side, unit circle, waves)" '\n')
    if trigmode == "angle":
        knownSide1 = input("First given side in relation to unknown angle? (hyp, opp, adj)")
        knownSide1Length = float(input("Length of this side?"))
        knownSide2 = input("Second given side in relation to unkown angle? (hyp, opp, adj)")
        knownSide2Length = float(input("Length of this side?"))
        if knownSide1 == "hyp":
            Hyp = knownSide1Length
        elif knownSide1 == "opp":
            Opp = knownSide1Length
        elif knownSide1 == "adj":
            Adj = knownSide1Length
        else:
            break
        if knownSide2 == "hyp":
            Hyp = knownSide2Length
        elif knownSide2 == "opp":
            Opp = knownSide2Length
        elif knownSide2 == "adj":
            Adj = knownSide2Length
        else:
            break
        if (
    if trigmode == "side":
        knownAngle = float(input("Given angle in degrees?"))
        knownSide = input("Given side in relation to given angle? (hyp, opp, adj)")
        knownSideLength = float(input("Length of the known side?"))
        unknownSide = input("Side we are solving for? (hyp, opp, adj)")
        if knownSide = unknownSide
            print("That's impossible, dude.")
            break

    if trigmode == "unit circle":
    if trigmode == "waves":
else:
    print("That isn't a function of this calculator.")
