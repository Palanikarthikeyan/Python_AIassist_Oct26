class P1:
    pass
class P2(P1):
    pass
class P3(P2):
    pass
class P4(P3):
    pass

# P1
# |
# P2
# |
# P3
# |
# P4
# ..
# --------------//Multi-Level 

class Pa:
    pass
class Pb:
    pass

class Pc(Pa,Pb):
    pass
# ----------------------------------//Multiple Inheritance 