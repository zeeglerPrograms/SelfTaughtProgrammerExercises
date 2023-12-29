#OOPStuff

class PublicPrivatExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    
    def public_method(self):
        # clients can use this
        pass

    def _unsafe_method(self):
        # clients shouldnt use this
        pass

#polymorphism
shapes = [tr1, sw1, cr1]
for a_shape in shapes:
    a_shape.draw()