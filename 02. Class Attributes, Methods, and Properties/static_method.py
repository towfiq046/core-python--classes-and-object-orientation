class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self._serial = ShippingContainer._generate_serial()


c1 = ShippingContainer("HIO", ["something"])
print(c1.next_serial)
print(ShippingContainer.next_serial)
c2 = ShippingContainer("ORB", ["Spam"])
print(c2.next_serial)
c3 = ShippingContainer("BIJ", ["Egg"])
print(c3.next_serial)
print(ShippingContainer.next_serial)
