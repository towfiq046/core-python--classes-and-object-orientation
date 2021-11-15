class ShippingContainer:

    next_serial = 1337

    # 2 ways to associate methods with the class.
    # 1. Static method
    # 2. Class method
    def _generate_serial(self):     # Here self is redundant.
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self._contents = contents
        self._serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


c1 = ShippingContainer("HIO", ["something"])
c2 = ShippingContainer("ORB", ["Spam"])
c3 = ShippingContainer("BIJ", ["Egg"])


print(c1.next_serial)
print(c2.next_serial)

print(ShippingContainer.next_serial)
