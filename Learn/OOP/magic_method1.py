class SpecicalString:
    def __init__(self,cont):
        self.cont = cont
    
    def __gt__(self,other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index]