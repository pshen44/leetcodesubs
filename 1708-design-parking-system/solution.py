class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lot = [big, medium, small]
        # big = 1
        # med = 2
        # small = 3

    def addCar(self, carType: int) -> bool:
        for i, slot in enumerate(self.lot):
            lottype = i + 1
            if lottype == carType:
                if slot:
                    self.lot[i] -= 1
                    return True
                else:
                    return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
