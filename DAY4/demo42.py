class Pa:
    pass

class Pb(Pa):
    pass

class Pc(Pa,Pb):
    pass

# obj = Pc() 
# TypeError: Cannot create a 
# consistent method resolution order (MRO) for bases Pa, Pb
