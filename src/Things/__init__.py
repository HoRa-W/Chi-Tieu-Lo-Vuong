class Thing:
    def __init__(self, Thing, Price):
        self.Thing = Thing
        self.Price = Price
    def UpdatePrice(self, newPrice):
        self.Price += newPrice

    def GetInfoThing(self):
        return self.Thing, self.Price

        
