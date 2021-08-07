class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity - v >= 0

    def add(self, v):
        self.capacity -= v


wallet = MoneyBox(50)
if wallet.can_add(51):
    wallet.add(51)
    print("added 51")
else:
    print("no i cant")

if wallet.can_add(48):
    wallet.add(48)
    print("added 48")
else:
    print("no i cant")
